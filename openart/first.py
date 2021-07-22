from machine import UART
import pyb
#form pyb import json
import sensor, image, time, math
import os, nncu




SHOW=True
state=2          #0为识别数字态   1为TAG码态  2为动物水果态
roi_rect=(0,25,300,120)
rect_threshold=50000
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA) # we run out of memory if the resolution is much bigger...
sensor.set_brightness(1800) # 设置图像亮度 越大越亮
sensor.skip_frames(time = 20)
sensor.set_auto_gain(True)         #自动增益
sensor.set_auto_whitebal(True)     #白平衡
sensor.set_auto_exposure(True)     #自动曝光
clock = time.clock()



uart = UART(1, baudrate=115200)     # 初始化串口 波特率设置为115200 TX是B12 RX是B13
tag_vale = number_vale = animals_fruit_vale = animals_fruit_con = number_con = 0x00



CMD_nofind_animals_fruit=[0xEE,0xBB,0x04,animals_fruit_con,0xFF]
CMD_nofind_number=[0xFF,0xBB,0x04,number_con,0xFF]




#number_labels = ["0","1","2","3","4","5","6","7",'8","9"]
number_labels = [line.rstrip() for line in open("/sd/number_models/labels_number.txt")]  # 加载标签
number_net = nncu.load("/number_models/_1s_model_05_0.9986_xxxx.nncu", load_to_fb=True)
#animals_fruit_labels =["cat","dog","horse","pig","casttle"，"apple"，"orange"，"banana"，"durian","grape"]
animals_fruit_labels = [line.rstrip() for line in open("/sd/animal_fruit_models/labels_animal_fruits.txt")]  # 加载标签
animals_fruit_net = nncu.load("/animal_fruit_models/_1s_model_25_0.9936_xxxx.nncu", load_to_fb=True)


## NNCU net
def nncu_detect(img1,net):
    scores = nncu.classify(net , img1)[0].output()
    max_score = max(scores)
    if(max_score>0.95):
        max_label = scores.index(max_score)
        return (max_label,max_score)
    return (None,0)




while(True):
    t0 = time.ticks()
    img = sensor.snapshot()
    uart_num = uart.any()       # 获取当前串口数据数量

    if(uart_num>0):
        uart_str = uart.read(1).strip()
        if(uart_str==b'\x01'):
            state=0
            uart.write('我现在接受的是01')
        elif(uart_str==b'\x02'):
            state=1
        elif(uart_str==b'\x03'):
            state=2




    if    state==0:
           result = number_net.classify(img,roi = ((320-160)//2,25,160,120))[0].output()
           max_score = max(result)
           max_label = result.index(max_score)
           #print(max_label , max_score)
           if(SHOW == True):
                 img.draw_string((320-160)//2 + 80, 5, str(max_label)+str(":")+ str(max_score),color = (0,255,0), scale = 2,mono_space=False)
                 img.draw_rectangle(((320-160)//2,25,160,120), color = (255, 0, 0))

           #串口发送
           number_vale=int(max_label)
           CMD_find_number=[0xEE,0xAA,0x02,number_vale,0xFF]
           uart.write(bytearray(CMD_find_number))


    elif  state==1 :
          for tag in img.find_apriltags(families=image.TAG25H9):
               if(tag.id()<10):

                   #串口通信
                   tag_vale=int(tag.id())
                   CMD_find_tag=[0xEE,0xAA,0x01,tag_vale,0xFF]
                   uart.write(bytearray(CMD_find_tag))
                   if(SHOW==True):
                     img.draw_rectangle(tag.rect(), color = (255, 0, 0))
                     img.draw_cross(tag.cx(), tag.cy(), color = (0, 255, 0))
                     print("Tag ID %d" % tag.id())

               else :
                  pass
    elif  state==2 :

            # ROI区域
            if(SHOW==True):
                 img.draw_rectangle(roi_rect, color = (0, 255, 0))
            for r in img.find_rects(threshold = rect_threshold,roi = roi_rect ) :
                 #差比和太大 - 非正方形   方框太小  不可能
                 if(r.rect()[3]/r.rect()[2]>1.3 or r.rect()[3]/r.rect()[2]<0.6):
                      break
                 if(abs(r.rect()[3]) < 40 or abs(r.rect()[2]) < 40):
                      break
                 #模型推理
                 img1 = img.copy(r.rect())
                 (result_obj,result_score)=nncu_detect(img1,animals_fruit_net)

                 #是否画图（找到的外接矩形及内点）
                 if(SHOW == True):
                     print(result_obj , result_score )
                     for p in r.corners():
                         img.draw_circle(p[0], p[1], 5, color = (0, 255, 0))
                     img.draw_rectangle(r.rect(), color = (255, 0, 0))
                 #串口通信
                 x_vale=int((r.rect()[0] + r.rect()[2]/2)/2)
                 y_vale=int((r.rect()[1] + r.rect()[3]/2)/2)
                 animals_fruit_vale=int(result_obj)
                 CMD_find_animals_fruit=[0xEE,0xAA,0x03,animals_fruit_vale,x_vale,y_vale,0xFF]
                 uart.write(bytearray(CMD_find_animals_fruit))


    #print(time.ticks()-t0)
    #画出中点，辅助快速打靶标定
    img.draw_cross(int(160), int(120), color = (0, 0, 255))

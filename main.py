import sys
import machine
import network
import ws2812 as ws2812
import wifi_connect as wifi_connect


#wifi
Wifi_info = (["www.qiwen.cn","miao13006331630"],["WHDC","whdc5325"],["MKNET","83842911"])
Mywifi = [Wifi_info[2][0], Wifi_info[2][1]]
#Pin
Led_PIN = 2
Led_NUM = 30

try:
    wifi_connect.do_connect(Mywifi[0],Mywifi[1])
    ws2812.init(data_pin=Led_PIN, leds_num=Led_NUM)
    ws2812.demo4()

except:
    wifi_connect.wifioff()




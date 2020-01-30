from machine import Pin
from neopixel import NeoPixel
import time

def init(data_pin, leds_num):
    global np

    dp = Pin(data_pin, Pin.OUT)
    np = NeoPixel(dp, leds_num)
    clear()

# 按红、绿、蓝、白显示灯带
def demo0():
    color = [(255,0,0),(0,255,0),(0,0,255),(255,255,255)]    #红、绿、蓝、白
    for i in range(0,np.n):
        np[i] = color[i%4]
    np.write()

# 白色循环2圈
def demo1():
    n = np.n
    for i in range(2 * n):
        for j in range(n):
            np[j] = (0, 0, 0)
        np[i % n] = (255, 255, 255)
        np.write()
        time.sleep_ms(25)
    clear()

# 蓝色走马灯
def demo2():
    n = np.n
    for i in range(2 * n):
        for j in range(n):
            np[j] = (0, 0, 128)
        if (i // n) % 2 == 0:
            np[i % n] = (0, 0, 0)
        else:
            np[n - 1 - (i % n)] = (0, 0, 0)
        np.write()
        time.sleep_ms(60)

# 黄色褪色呼吸灯
def demo3():
    n = np.n
    for i in range(0, 4 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            np[j] = (val, 0, 0)
            print(val)
        np.write()

# 黄色呼吸灯
def demo4():
    n = np.n
    for i in range(0, 4 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            np[j] = (val, val, 0)
        np.write()
        

# 魔方灯样式1
def demo5():
    #color = [(255,0,0),(0,128,0),(255,165,0),(0,0,255),(255,255,0),(255,255,255)]    #红、绿、橙、蓝、黄、白
    color = [(55,0,0),(0,128,0),(55,55,0),(0,0,55),(55,55,0),(55,55,55)]    #红、绿、橙、蓝、黄、白
    MF = [
        [[0, 1, 2, 3], [16, 17, 18, 19],[32, 33, 34, 35]],
        [[4, 5, 6, 7], [20, 21, 22, 23], [36, 37, 38, 39]],
        [[8, 9, 10, 11], [24, 25, 26, 27], [40, 41, 42, 43]],
        [[12, 13, 14, 15], [28, 29, 30, 31], [44, 45, 46, 47]]
    ]
    while True:
        for nn in range(16):
            for m in range(4):   
                for x in MF[m]:
                    for y in x:
                        np[(y+nn)-16]=color[m]                
                np.write()
                time.sleep_ms(10)



def clear():
    n = np.n
    for i in range(n):
        np[i] = (0, 0, 0)
    np.write()

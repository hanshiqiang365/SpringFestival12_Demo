#author: hanshiqiang365 （微信公众号）
import sys
import time
import ctypes
import winsound

STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE = -12

FOREGROUND_BLUE = 0x09          # 蓝色
FOREGROUND_GREEN = 0x0a         # 绿色
FOREGROUND_RED = 0x0c           # 红色
FOREGROUND_YELLOW = 0x0e        # 黄色
FOREGROUND_WHITE = 0x0f         # 白色

std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

def set_cmd_text_color(color, handle=std_out_handle):
    Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return Bool

def resetColor():
    set_cmd_text_color(FOREGROUND_WHITE)

def cprint(mess, color):
    color_dict = {
                  '蓝色': FOREGROUND_BLUE,
                  '绿色': FOREGROUND_GREEN,
                  '红色': FOREGROUND_RED,
                  '黄色': FOREGROUND_YELLOW,
                  '白色': FOREGROUND_WHITE
                 }
    set_cmd_text_color(color_dict[color])
    print(mess)
    resetColor()

def view_bar(num,total):
    rate = num / total
    rate_num = int(rate * 100)
    r = '\r%s>%d%%' % ('=' * rate_num, rate_num,)
    sys.stdout.write(r)
    sys.stdout.flush

def biu():
    for x in range(12):
        cprint('~Biu~oOo~Biu~'.center(100),'红色')
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
        time.sleep(1)

def sitdown():
    for x in range(12):
        cprint('| ~ ~ |'.center(100),'蓝色')
        time.sleep(0.5)

def process():
    for i in range(0, 101):
        time.sleep(0.1)
        view_bar(i, 100)
        
if __name__ == '__main__':
    print("春节十二响程序启动:")
    time.sleep(1)
    print("程序加载进度:")
    time.sleep(1)
    process();
    print("程序加载完毕...")
    time.sleep(1)
    print("硬件系统自检完成...")
    time.sleep(1)
    print("撞针系统自检完成...")
    time.sleep(1)
    print("行星发动机正在启动...")
    cprint(' '.center(100),'红色')
    biu();
    cprint('oOo'.center(100),'红色')
    cprint('\ ~ ~ /'.center(100),'蓝色')
    sitdown();
    time.sleep(0.5)
    cprint('/--  --\\'.center(100),'蓝色')
    time.sleep(0.5)
    cprint('\  /'.center(100),'蓝色')
    time.sleep(0.5)
    cprint('|--------|'.center(100),'黄色')
    time.sleep(0.5)
    cprint('---------------------------'.center(100),'黄色')


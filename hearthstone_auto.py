import cv2 as cv
import time
from PIL import ImageGrab
import pyautogui as pymouse
import math


def mouse_drag_from_to(fromx, fromy, tox, toy):
    pymouse.moveTo(fromx, fromy)
    # duration 表示的是持续的时间
    pymouse.dragTo(tox, toy, duration=0.3)


# 鼠标点击事件
def mouse_click(inx, iny):
    pymouse.click(inx, iny)


# 选定随从进行攻击
def attack():
    mouse_click(770,910)
    time.sleep(0.5)
    mouse_click(1298, 276)
    mouse_click(900,910)
    time.sleep(0.5)
    mouse_click(1298, 276)
    mouse_click(1050,910)
    time.sleep(0.5)
    mouse_click(1298, 276)
    mouse_click(1200,910)
    time.sleep(0.5)
    mouse_click(1298, 276)
    mouse_click(1350,910)
    time.sleep(0.5)
    mouse_click(1298, 276)
    mouse_click(1500,910)
    time.sleep(0.5)
    mouse_click(1298, 276)
    mouse_click(1650,910)
    time.sleep(0.5)
    mouse_click(1298, 276)

# 出牌
def cards_out():
    # 把每一张牌抓一遍
    mouse_drag_from_to(854, 1429, 1260, 920)
    mouse_drag_from_to(950, 1429, 1260, 920)
    mouse_drag_from_to(1050, 1429, 1260, 920)
    mouse_drag_from_to(1150, 1429, 1260, 920)
    mouse_drag_from_to(1250, 1429, 1260, 920)
    mouse_drag_from_to(1350, 1429, 1260, 920)
    mouse_drag_from_to(1450, 1429, 1260, 920)
    mouse_drag_from_to(1550, 1429, 1260, 920)
    mouse_drag_from_to(1650, 1429, 1260, 920)
    mouse_drag_from_to(1750, 1429, 1260, 920)



# 计算方差
def getss(list):
    # 计算平均值
    avg = sum(list) / len(list)
    # 定义方差变量ss，初值为0
    ss = 0
    # 计算方差
    for l in list:
        ss += (l - avg) * (l - avg) / len(list)
    # 返回方差
    return ss


# 获取每行像素平均值
def getdiff(img):
    # 定义边长
    Sidelength = 30
    # 缩放图像
    img = cv.resize(img, (Sidelength, Sidelength), interpolation=cv.INTER_CUBIC)
    # 灰度处理
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # avglist列表保存每行像素平均值
    avglist = []
    # 计算每行均值，保存到avglist列表
    for i in range(Sidelength):
        avg = sum(gray[i]) / len(gray[i])
        avglist.append(avg)
    # 返回avglist平均值
    return avglist



# 检测相似度
def detect_and_return_probability(pix, x1, y1, x2, y2):
    time.sleep(1.3)
    # 截取屏幕快照
    temp = ImageGrab.grab(bbox=(x1, y1, x2, y2))  # x1,y1,x2,y2
    temp.save("images/temp.jpg")
    img1 = cv.imread("images/temp.jpg")
    img2 = cv.imread(pix)
    diff1 = getdiff(img1)
    diff2 = getdiff(img2)
    return abs(math.sqrt(getss(diff1))-math.sqrt(getss(diff2)))


while True:
    # 游戏开始
    time.sleep(5)
    # 点击开始游戏
    mouse_click(1940, 1295)
    # 等待60s匹配到了对手
    time.sleep(45)
    # 确认手牌
    mouse_click(1282, 1254)
    time.sleep(10)
    print("hello")
    # # 进行游戏
    # 读取测试图片
    # time.sleep(2)
    # detect_and_return_probability("images/my_turn_green.png", 2065, 688, 2261, 757);

    while True:
        mouse_click(500, 500)
        mouse_click(500, 500)
        # print(detect_and_return_probability("images/my_turn_yellow.jpg", 2065, 688, 2261, 757))
        # 我的回合且可以出牌

        if detect_and_return_probability("images/my_turn_yellow.jpg", 2065, 688, 2261, 757)< 5:
            print("到我的回合了，我开始出牌")
            cards_out()
            time.sleep(10)
            # 随从进行攻击
            print("随从开始攻击")
            attack()
            # 点击回合结束
            # 英雄攻击
            print("英雄开始攻击")
            mouse_click(1554,1226)
            # attack(1554,1226)
            mouse_click(2165, 712)
            mouse_click(100, 100)
            print("攻击结束")
        # 对手回合
        elif detect_and_return_probability("images/enemy_turn.png", 1460, 460, 1600, 530) <5:
            print("这是对手的回合")
            time.sleep(3)
        # if detect_and_return_probability("images/start_game.png", 1270, 790, 1490,
        #                                  990) <5:  # 游戏结束多次点击后是否已经到了
        #     break

import pyautogui
import time
import sys
#运行需要pyautogui库，没有请在命令行使用pip install pyautogui命令安装
#刷普通难度2-4关第一个怪，运行python前确保炉石处于普通难度第二关的选怪界面
#炉石分辨率请用1600*900，调节后应自动居中，不是请重新调整
#佣兵队伍使用塞林，米尔豪斯，晨拥。塞林应装备驱除无冷却的装备
#佣兵队伍应为第一队（选择队伍界面第一个），添加顺序为塞林，晨拥，米尔豪斯，运行后检查塞林在场上最左，确保5回合能结束战斗，不能请修改turn到合理的回合数
turn = 5
#如出现严重色差问题无法运行，请使用auto2函数（修改最底下的auto1为auto2）


def auto1():
    time.sleep(3)
    while (True):
        try:
            pyautogui.click(573, 732)
           # print("a")
            time.sleep(1)
            pyautogui.click(1415, 817)
           # print("b")
            time.sleep(3)
            pyautogui.click(529, 394)
            time.sleep(1)
            pyautogui.click(1315, 817)
            time.sleep(2)
            pyautogui.click(869, 626)
           # print("c")
            time.sleep(9)
            pyautogui.click(1415, 817)
           # print("d")
            t = 0
            while ((not pyautogui.pixelMatchesColor(1464, 527, (146, 151, 22), tolerance=15)) and t < 6 and (not pyautogui.pixelMatchesColor(1025, 506, (63, 68, 129), tolerance=15))):
                time.sleep(5)
                t = t+1
               # print(t)
            time.sleep(1)
            pyautogui.click(1468, 517)
            if not pyautogui.pixelMatchesColor(1025, 506, (63, 68, 129), tolerance=15):
                time.sleep(30)
                #print("e")
            t = 0
            while(t < turn and (not pyautogui.pixelMatchesColor(1025, 506, (63, 68, 129), tolerance=15))):
                pyautogui.click(1120, 513)
                time.sleep(1.5)
                pyautogui.click(806, 520)
                time.sleep(1.5)
                pyautogui.click(806, 520)
                time.sleep(3)
                pyautogui.click(1468, 517)
                time.sleep(1)
                if pyautogui.pixelMatchesColor(1025, 506, (63, 68, 129), tolerance=15):
                    break
                pyautogui.click(1468, 517)
                time.sleep(19)
                #print("f")
                t = t+1
            #print("g")
            pyautogui.click(865, 567)
            time.sleep(1.5)
            pyautogui.click(1111, 822)
            time.sleep(5)
           # print("h")
            pyautogui.click(813, 941)
            time.sleep(1)
            pyautogui.click(1062, 764)
            time.sleep(1)
            pyautogui.click(866, 618)
            time.sleep(5)
            pyautogui.click(866, 618)
            time.sleep(5)
        except:
            time.sleep(1)
            print("error")


def auto2():
    time.sleep(3)
    while (True):
        try:
            pyautogui.click(573, 732)
           # print("a")
            time.sleep(1)
            pyautogui.click(1415, 817)
           # print("b")
            time.sleep(3)
            pyautogui.click(529, 394)
            time.sleep(1)
            pyautogui.click(1315, 817)
            time.sleep(2)
            pyautogui.click(869, 626)
           # print("c")
            time.sleep(9)
            pyautogui.click(1415, 817)
           # print("d")
            time.sleep(30)
            pyautogui.click(1468, 517)
            time.sleep(25)
            t = 0
            while(t < turn):
                pyautogui.click(1120, 513)
                time.sleep(1.5)
                pyautogui.click(806, 520)
                time.sleep(1.5)
                pyautogui.click(806, 520)
                time.sleep(3)
                pyautogui.click(1468, 517)
                time.sleep(1)
                pyautogui.click(1468, 517)
                time.sleep(19)
                #print("f")
                t = t+1
            #print("g")
            pyautogui.click(865, 567)
            time.sleep(1.5)
            pyautogui.click(1111, 822)
            time.sleep(5)
           # print("h")
            pyautogui.click(813, 941)
            time.sleep(1)
            pyautogui.click(1062, 764)
            time.sleep(1)
            pyautogui.click(866, 618)
            time.sleep(5)
            pyautogui.click(866, 618)
            time.sleep(5)
        except:
            time.sleep(1)
            print("error")


auto1()

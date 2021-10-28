import pyautogui
import time
import sys
import os
#运行需要pyautogui库，没有请在命令行使用pip install pyautogui命令安装
#刷普通难度2-4关第一个怪，运行python前确保炉石处于普通难度第二关的选怪界面
#炉石分辨率请用1600*900，调节后应自动居中，不是请调为其他分辨率后重新调整
#佣兵队伍使用塞林，米尔豪斯，晨拥。塞林应装备驱除无冷却的装备，理论上可以添加更多的佣兵练级，但请保证出场时塞林，米尔豪斯，晨拥在最左边三张
#佣兵队伍应为第一队（选择队伍界面第一个），添加顺序为晨拥，嘉顿，米尔豪斯，运行后检查塞林在场上最左，确保5回合能结束战斗，不能请修改turn到合理的回合数
turn = 5
#如出现严重色差问题无法运行，请使用2模式

#单刷1-1脚本，运行python前确保炉石处于第一关地图选怪界面，请输入关数(目前只支持1-1，不要修改)，以及使用的佣兵队伍位置（从左往右，从上往下以此为1-9，佣兵队伍应只包含一人）
# 希望使用的非指向性技能（1-3，不用请输入0，不支持指向技能），最大战斗回合（单场战斗不应超过此回合，建议输8以上）
# 使用前请确保单佣兵单技能打的过
level_ = 1  # 关数
team_ = 3  # 队伍位置
skill_ = 3  # 技能
turn_ = 8  # 最大回合

#选择模式,1为刷2-4， 2为无色差模式， 3为单刷模式
mode = 3


def auto1():
    time.sleep(3)
    flag = True
    while (True):
        try:
            if flag:
                pyautogui.click(573, 732)
                #print("a")
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
            else:
               # print("d1")
                flag = True
                time.sleep(5)
            t = 0
            while ((not pyautogui.pixelMatchesColor(1464, 527, (146, 151, 22), tolerance=15)) and t < 6
                   and (not pyautogui.pixelMatchesColor(1025, 506, (63, 68, 129), tolerance=10))
                   and (not pyautogui.pixelMatchesColor(1025, 506, (63, 90, 63), tolerance=10))
                   and (not pyautogui.pixelMatchesColor(1025, 506, (125, 44, 26), tolerance=10))):
               # print(pyautogui.pixel(1025, 506))
                time.sleep(5)
                t = t+1
               # print(t)
            time.sleep(1)
            pyautogui.click(1468, 517)
            if not pyautogui.pixelMatchesColor(1025, 506, (63, 68, 129), tolerance=15) and (not pyautogui.pixelMatchesColor(1025, 506, (63, 90, 63), tolerance=15)) and (not pyautogui.pixelMatchesColor(1025, 506, (125, 44, 26), tolerance=15)):
                time.sleep(30)
                #print("e")
            t = 0
            while(t < turn and (not pyautogui.pixelMatchesColor(1025, 506, (63, 68, 129), tolerance=15))
                  and (not pyautogui.pixelMatchesColor(1025, 506, (63, 90, 63), tolerance=15))
                  and (not pyautogui.pixelMatchesColor(1025, 506, (125, 44, 26), tolerance=15))):
                pyautogui.click(1120, 513)
                time.sleep(1.5)
                pyautogui.click(806, 520)
                time.sleep(1.5)
                pyautogui.click(806, 520)  # (952,507)##
                time.sleep(3)
                pyautogui.click(1468, 517)
                time.sleep(1)
                if pyautogui.pixelMatchesColor(1025, 506, (63, 68, 129), tolerance=15) or pyautogui.pixelMatchesColor(1025, 506, (63, 90, 63), tolerance=15) or pyautogui.pixelMatchesColor(1025, 506, (125, 44, 26), tolerance=15):
                    break
                pyautogui.click(1468, 517)
                time.sleep(19)
                #print("f")
                t = t+1
            #print("g")
            pyautogui.click(865, 567)
            time.sleep(1.5)
            pyautogui.click(1111, 822)
            time.sleep(8)
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
            flag = False
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


def prepare(s, s1):
    pyautogui.click(559+((s-1) % 3)*263, 423+((s-1)//3)*309)  # (573, 732,822)
    # print("a")
    time.sleep(1)
    pyautogui.click(1415, 817)
    # print("b")
    time.sleep(4)
    pyautogui.click(529+((s1-1) % 3)*221, 394+((s1-1)//3)*131)  # (529, 394)
    time.sleep(1)
    pyautogui.click(1315, 817)
    time.sleep(2)
    pyautogui.click(869, 626)
    # print("c")
    time.sleep(9)
    pyautogui.click(1415, 817)


def battle(t1, s):
    t = 0
    while (t < t1 and (not pyautogui.pixelMatchesColor(1025, 506, (63, 68, 129), tolerance=15))
           and (not pyautogui.pixelMatchesColor(1025, 506, (63, 90, 63), tolerance=15))
           and (not pyautogui.pixelMatchesColor(1025, 506, (125, 44, 26), tolerance=15))):
        if s == 3:
            pyautogui.click(1120, 513)
            time.sleep(1.5)
        elif s == 2:
            pyautogui.click(952, 507)
            time.sleep(1.5)
        elif s == 1:
            pyautogui.click(806, 520)
            time.sleep(1.5)
        time.sleep(1.5)
        pyautogui.click(1468, 517)
        time.sleep(1)
        if pyautogui.pixelMatchesColor(1025, 506, (63, 68, 129), tolerance=15) \
                or pyautogui.pixelMatchesColor(1025, 506, (63, 90, 63), tolerance=15) \
                or pyautogui.pixelMatchesColor(1025, 506, (125, 44, 26), tolerance=15)  \
                or pyautogui.pixelMatchesColor(1553, 412, (6, 4, 3), tolerance=15):
            break
        pyautogui.click(1468, 517)
        time.sleep(14)
        # print("f")
        t = t + 1


def deploy():
    t = 0
    while ((not pyautogui.pixelMatchesColor(1464, 527, (146, 151, 22), tolerance=15)) and t < 6):
        # print(pyautogui.pixel(1025, 506))
        time.sleep(5)
        t = t + 1
    # print(t)
    time.sleep(1)
    pyautogui.click(1468, 517)
    if not pyautogui.pixelMatchesColor(1025, 506, (63, 68, 129), tolerance=15) and (
            not pyautogui.pixelMatchesColor(1025, 506, (63, 90, 63), tolerance=15)) and (
            not pyautogui.pixelMatchesColor(1025, 506, (125, 44, 26), tolerance=15)):
        time.sleep(10)


def choose():
    pyautogui.click(865, 567)
    time.sleep(1.5)
    pyautogui.click(1111, 822)
    time.sleep(5)


def auto3(level=1, team=1, skill=3, turn1=6):
    time.sleep(3)
    flag = 0
    while (True):
        try:
            if pyautogui.pixelMatchesColor(1047, 217, (189, 89, 132), tolerance=15):
                flag = 0
            if flag == 0:
                prepare(level, team)
                flag = flag+1
               # print("d")
            else:
               # print("d1")
                time.sleep(5)
            if flag == 1:
                deploy()
                flag = flag+1
                #print("e")
            if flag == 2:
                battle(turn1, skill)
                flag = flag+1
                choose()
            #print("g")
            if flag == 3:
                pyautogui.click(911, 523)
                time.sleep(1)
                pyautogui.click(1018, 523)
                time.sleep(1)
                pyautogui.click(1415, 817)
                time.sleep(1)
                flag = flag+1
            if flag == 4:
                deploy()
                flag = flag + 1
            if flag == 5:
                battle(turn1, skill)
                flag = flag + 1
                choose()
            if flag == 6:
                pyautogui.click(810, 530)
                time.sleep(1)
                pyautogui.click(1415, 817)
                time.sleep(1)
                flag = flag + 1
            if flag == 7:
                deploy()
                flag = flag + 1
            if flag == 8:
                battle(turn1, skill)
                flag = flag + 1
                choose()
                pyautogui.click(1415, 817)
                time.sleep(1)
            if flag == 9:
                deploy()
                flag = flag + 1
            if flag == 10 and (not pyautogui.pixelMatchesColor(1047, 217, (189, 89, 132), tolerance=15)):
                battle(turn1, skill)
                time.sleep(8)
                pyautogui.click(1001, 384)
                time.sleep(1.5)
                pyautogui.click(744, 769)
                time.sleep(1.5)
                pyautogui.click(1268, 786)
                time.sleep(1.5)
                pyautogui.click(984, 614)
                time.sleep(10)
                pyautogui.click(951, 840)
                time.sleep(3)
            if pyautogui.pixelMatchesColor(1047, 217, (189, 89, 132), tolerance=15):
                flag = 0
        except:
            time.sleep(1)
            print("error")


'''
time.sleep(5)
while(True):
    try:
        print(pyautogui.pixel(1553, 412))
        break
    except:
        print("a")
'''
if mode == 1:
    auto1()
elif mode == 2:
    auto2()
elif mode == 3:
    auto3(level_, team_, skill_, turn_)

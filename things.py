# encoding: utf-8
# @Author: 550W
import os, time

foods = {"鸡腿": (6, 10), "汉堡": (5, 15), "薯条": (4, 15), "可乐": (3, 10), "泡面": (5, 20), "答辩": (0, 2),
         "马尿": (0, 1)}
# foods 的key是食物名称，value[0]是价格,value[1]是饱食度
toys = {""}

RMB = 0
sat = 100
happy = 100


def hungry():
    global RMB, sat, happy
    i = 1
    food_money = []
    pick = {}
    print("=====侯饿了=====")
    print("(* _ *)_-P")
    print("请选择投喂的食物")
    for name in foods:
        print(f"{name} {foods[name][0]}￥ 饱食度{foods[name][1]}({i})")
        food_money.append(foods[name][0])
        pick[i] = name
        i += 1
    print(f"[Info]当前你有{RMB}￥")
    if RMB < min(food_money):
        print("[Exit]你穷逼，没有足够的钱")
        return None
    index = input(">请输入你要投喂的食物编号：")
    if not index.isdigit():
        print("[Exit]输入内容非数字，已停止投喂")
        return None
    index = int(index)
    if index > i:
        print("[Exit]输入编号超出范围，已停止投喂")
        return None
    if foods[pick[index]][0] != 0:
        print("ヾ(≧▽≦*)oヾ")
        RMB -= foods[pick[index]][0]
        happy += 35
    else:
        print("(╯‵□′)╯")
        happy += 10
    sat += foods[pick[index]][1]
    print(f"[Info]你已投喂{pick[index]}")
    print(f"[Info]当前你还有{RMB}￥")
    print(f"[Info]侯瑞饱食度{sat}")
    print(f"[Info]侯瑞心情值{happy}")
    print("三秒后退出")
    time.sleep(3)
    os.system("cls")


def monkey_kill_you():
    command = {"/help": "都开源了，还要提示吗？", "/ach": "你获得了一个隐藏成就“归西”"}
    print("=====侯急了=====")
    print("//||(X _ X)|||||==╰(艹皿艹 )")
    print("侯瑞心态十分炸裂，她杀了你！")
    res = input("请输入你的遗言:")
    if res[0] == '/' and res != "/exit":
        try:
            print(command[res])
        except:
            ...
    print("[Exit]三秒后退出游戏")
    time.sleep(3)
    exit(114514)


def starve():
    print("=====侯死了=====")
    print("<(X _ X)>")
    print("侯瑞已经饿死了，已退出")
    if input("请输入留言:") == "好开心":
        print("解锁结局：“少了一个累赘”")
        os.system("pause")
        exit()
    print("[Exit]三秒后退出游戏")
    time.sleep(3)
    exit(114514)


if __name__ == '__main__':
    monkey_kill_you()

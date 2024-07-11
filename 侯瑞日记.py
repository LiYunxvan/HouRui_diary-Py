# encoding:utf-8
# @Author: 550W

import os
import things as t

day = 0
while True:
    os.system("cls")
    t.RMB += 10
    day += 1
    t.sat -= 10
    t.happy -= 10
    print(f"------第{day}天------")
    if t.sat > 20 and t.happy > 20:
        print("无事发生")
        os.system("pause")
        continue
    if t.happy <= 0:
        t.monkey_kill_you()
    if t.sat <= 10:
        t.starve()
    if t.sat <= 20:
        t.hungry()
    os.system("pause")
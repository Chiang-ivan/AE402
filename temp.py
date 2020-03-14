# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random

n=random.randint(1,10)

c=True

for i in range(5):  
    ans=int(input("請輸入答案:"))

    if ans == n:
        print("答對了!")
        False
    if ans > n:
        print("太大")
    
    if ans < n:
        print("太小")



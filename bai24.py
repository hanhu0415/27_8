# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 13:08:57 2024

@author: DELL
"""

thoigian=input("Nhap thoi gian theo dinh dang hh:mm:ss ")
hh, mm, ss = map(int, thoigian.split(':'))
if 0<=hh<=24 and 0<=mm<=60 and 0<=ss<=60:
    print("Thời gian hợp lệ.")
else:
    print("Thời gian không hợp lệ!!")
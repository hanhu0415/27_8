# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:03:37 2024

@author: DELL
"""

thoigian=input("Nhap thoi gian theo dinh dang hh:mm:ss ")
hh, mm, ss = map(int, thoigian.split(':'))
print("Tong thoi gian doi sang giay la: ", hh*3600 + mm*60 + ss)
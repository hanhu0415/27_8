# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 12:08:04 2024

@author: DELL
"""

thoigian=input("Nhap thoi gian theo dinh dang ..h..p..s:  ")
so=""
for i in thoigian:
  if i.isalpha():
      so += ":"
  else:
      so += i
so_cuoi=so[:-1]
hh, mm, ss = map(int, so_cuoi.split(':'))
print(thoigian,"đổi sang giây là: ", hh*3600 + mm*60 + ss)
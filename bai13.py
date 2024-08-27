# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:48:14 2024

@author: DELL
"""
thoigian=input("Nhap thoi gian theo dinh dang dd mm yyyy: ")
dd, mm, yy = thoigian.split(' ')
print(f"a. {dd}/{mm}/{yy}")
print(f"b. {dd}/{mm}/{yy[2:]}")
print(f"c. {yy}/{mm}/{dd}")
thoigian1=input("Nhap thoi gian theo dinh dang dd/mm/yyyy: ")
d, m, y = thoigian1.split('/')
print(f"a. {d} {m} {y}")
print(f"b. {d} {m} {y[2:]}")
print(f"c. {y} {m} {d}")
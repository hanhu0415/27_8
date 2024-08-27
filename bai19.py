# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 12:51:26 2024

@author: DELL
"""

a=int(input("Nhập a: "))
b=int(input("Nhập b: "))
c=int(input("Nhập c: "))
d=int(input("Nhập d: "))
be_nhat=a
if a>b:
    be_nhat=b
if a>c:
    be_nhat=c
if a>d:
    be_nhat=d
print("Số bé nhất là:", be_nhat)
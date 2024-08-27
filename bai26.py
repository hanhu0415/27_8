# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 17:54:46 2024

@author: DELL
"""

a=float(input("Nhập a: "))
b=float(input("Nhập b: "))
c=float(input("Nhập c: "))
if a>b:
    x=a
    a=b
    b=x
if a>c:
    x=a
    a=c
    c=x
if b>c:
    x=b
    b=c
    c=x
print("a. Sắp xếp theo thứ tự tăng dần: ",a,b,c)
 
d=input("b. Nhập số nguyên N: ")
d1=list(d)
d2=sorted(d1)
print("Sắp xếp: ", "".join(d2))

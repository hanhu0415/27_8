# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 12:29:27 2024

@author: DELL
"""

a=input("Nhập thời gian theo định dạng hh:mm:ss ")
b=input("Nhập thời gian theo định dạng hh:mm:ss ")
hh, mm, ss = map(int, a.split(':'))
h, m, s = map(int, b.split(':'))
x=(hh*3600)+(mm*60)+ss
y=(h*3600)+(m*60)+s
hieu=x-y
if hieu>0: 
    h1=hieu//3600
    m1=(hieu%3600)//60
    s1=hieu%60
    print(f"Hiệu thời gian là: {h1}h {m1}p {s1}s")
else:
    print("Không thể trừ hai thời gian này")
tong=x+y
h2=tong//3600
m2=(tong%3600)//60
s2=tong%60
print(f"Tổng thời gian là: {h2}h {m2}p {s2}s")

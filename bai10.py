# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:14:41 2024

@author: DELL
"""

m=int(input("Nhập biển số xe của bạn: "))
a=m//1000
b=(m%1000)//100
c=(m%100)//10
d=m%10
ab=a+b+c+d
g=ab//10
h=ab%10
nut=g+h
x=nut//10
y=nut%10
nut1=x+y
print("Biển số của bạn có ",nut1," nút.")
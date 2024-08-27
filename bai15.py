# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 19:32:55 2024

@author: DELL
"""
import math
a=float(input("Nhap a: "))
b=float(input("Nhap b: "))
x=a**(1/3)
y=b**(1/3)
ab=(a*b)**(1/3)
print(" Ket qua la: ", ((a+b)/(x+y))/(math.sqrt(x+y)))
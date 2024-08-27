# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:40:03 2024

@author: DELL
"""
print("Nhập 'v' nếu muốn tính chu vi, diện tích hình vuông")
print("Nhập 'n' nếu muốn tính chu vi, diện tích hình chữ nhật")
print("Nhập 't' nếu muốn tính chu vi, diện tích hình tròn")
a=input("Nhập hình: ")
if a=="v":
    v=float(input("Nhập độ dài cạnh: "))
    print("Chu vi hình vuông là: ", v*4)
    print("Diện tích hình vuông là: ", v*v)
elif a=="n":
    d=float(input("Nhập chiều dài hình chữ nhật: "))
    r=float(input("Nhập chiều rộng hình chữ nhật: "))
    print("Chu vi hình chữ nhật là: ", (d+r)*2)
    print("Diện tích hình chữ nhật là: ", d*r)
elif a=="t":
    b=float(input("Nhập bán kính hình tròn: "))
    print("Chu vi hình tròn là: ",3.14*2*b)
    print("Diện tích hình tròn là: ",3.14*(b*b))
else:
    print("Vui lòng nhập đúng cú pháp!")
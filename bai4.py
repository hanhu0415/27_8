# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:02:49 2024

@author: DELL
"""

a=int(input("Nhap a: "))
if 10<=a<=99:
    hang_chuc=a%10
    hang_donvi=a//10
    tong=hang_chuc+hang_donvi
    print("Tong cua ", hang_chuc," va", hang_donvi," la: ", tong)
else:
    print("Chi nhap so co hai chu so!")
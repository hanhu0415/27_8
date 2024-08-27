# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 17:49:50 2024

@author: DELL
"""

s=input("Nhập kí tự: ")
if len(s)==1:
  if s==s.lower():
    print(s.upper())
  else:
    print(s.lower())
else:
    print("Chỉ nhậ một kí tự!")
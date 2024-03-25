# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 19:58:56 2024

@author: jyoti
"""

def multiplication_table(n):
    for i in range(1,11):
        print (n,'X',i,'=',n*i)
n=int(input('Enter the number: '))
result=multiplication_table(n)

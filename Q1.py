# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 16:57:07 2024

@author: jyoti
"""
def pattern_print(n):
    for i in range(n, 0, -1):
        print('*' * i)
    print()

n = int(input('Enter the number of rows: '))
pattern_print(n)
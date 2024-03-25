# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 19:12:16 2024

@author: jyoti
"""

def inch_to_cm(inch):
    cm=inch*2.54
    return cm
inch=float(input('Enter the inches : '))
cm=inch_to_cm(inch)
print('The',inch,' inch is',cm,' in centimeter')
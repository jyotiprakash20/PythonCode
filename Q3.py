# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 19:35:21 2024

@author: jyoti
"""
def remove_word(word_list, word_to_remove):
    new_list = [item.strip() for item in word_list if item.strip() != word_to_remove]
    return new_list
word_list = [' hello ', 'world', ' python ', 'function ', 'example ', 'remove_and_strip ', 'strip_word ', 'example2 ', 'example3 ']
word_to_remove = str(input('Enter the word to reomove: '))
new_list=remove_word(word_list,word_to_remove)
print(new_list)
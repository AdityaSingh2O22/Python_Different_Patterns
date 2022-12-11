# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 12:08:58 2022

@author: Aditya Singh
"""

"""
function
"""
def pattern(n,sign):
    for i in range(n):
        for j in range(i+1):
            print(sign,end=" ")
        print("\n")
    print()    
n=int(input("Enter the value of the N: "))    
sign=input("Enter the sign of the pattern: ")

# main 
pattern(n,sign)


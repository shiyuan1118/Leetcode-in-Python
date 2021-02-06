#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 22:32:26 2021

@author: baoshiyuan
"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res=[]
        
        carry=0
        l1=len(num1)-1
        l2=len(num2)-1
        
        
        while l1>=0 or l2>=0:
            if l1>=0:
                x1=ord(num1[l1])-ord('0')
            else:
                x1=0
            if l2>=0:
                x2=ord(num2[l2])-ord('0')   
            else:
                x2=0
            mod=(x1+x2+carry)%10
            carry=(x1+x2+carry)//10
            res.append(mod)
            l1-=1
            l2-=1
                       
        if carry:
            res.append(carry)
        
        return ''.join(str(x) for x in res[::-1])
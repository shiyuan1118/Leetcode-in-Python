#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 15:14:17 2021

@author: baoshiyuan
"""

class Solution:
    def myAtoi(self, s: str) -> int:
        stripS=s.strip()
        
        if stripS=="" or stripS=="+" or stripS=="-":
            return 0
        
        s1=re.match('[^\d]+',(stripS.lstrip("-")).lstrip("+"))
        
        if s1!=None:
            return 0
        else:
            s1=re.search('\-*\+*\d+',stripS).group()
            
        if s1[0:2]=="++" or s1[0:2]=="--" or s1[0:2]=="-+":
            return 0
      
        result=int(s1)
        
        if result>=0:
            if result>=2**31-1:
                return 2**31-1
            else:
                return result
        elif result<0:
            if result<=-2**31:
                return -2**31
            else:
                return result
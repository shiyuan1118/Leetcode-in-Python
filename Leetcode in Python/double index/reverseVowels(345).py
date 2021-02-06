#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 13:04:17 2020

@author: baoshiyuan
"""

#reverse vowels of string
class Solution:
    def reverseVowels(s):
        n=len(s)
        if n<=1:
            return s
        vowels=['a','e','i','o','u','A','E','I','O','U']
        i=0
        j=n-1
        result=list(s)
        while i<=j:
            if s[i] not in vowels:
                i+=1
            if s[j] not in vowels:
                j-=1
            if (s[i] in vowels) and (s[j] in vowels):
                result[i],result[j]=s[j],s[i]
                i+=1
                j-=1                
        return "".join(result)
print(Solution.reverseVowels('tianyu')) 
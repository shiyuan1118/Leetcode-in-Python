#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 13:08:33 2020

@author: baoshiyuan
"""

#Valid Palindrome 2
class Solution:
   def validPalindrome(s):
        i=0
        j=len(s)-1
        while i<=j:
            if s[i]!=s[j]:
               return Solution.isPalindrome(s,i+1,j) or Solution.isPalindrome(s,i,j-1)
            else:
               i+=1
               j-=1
        return True
      
   def isPalindrome(s,i,j):
        while i<=j:
            if s[i]!=s[j]:
                return False
            else:
                i+=1
                j-=1
        return True
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 15:23:52 2021

@author: baoshiyuan
"""

import math
class Solution:
    def judgeSquareSum(self,c):
        if c<=0:
           return 'no solution'
        r=int(math.sqrt(c))
        i=0
        j=r
        while i<=j:
            m=i*i+j*j
            if m==c:
                return True
            elif m<c:
                i+=1
            else:
                j-=1
        return False
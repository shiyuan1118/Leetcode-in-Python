#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 13:01:48 2020

@author: baoshiyuan
"""

#juedgeSquareSum(1)
import math
class Solution:
    def judgeSquareSum(c):
        if c<=0:
           return 'no solution'
        r=int(math.sqrt(c))+1
        for i in range(r):
           for j in range(r):
               m=i*i+j*j
               if m==c:
                    return True
               else:
                    continue
        return False

print(Solution.judgeSquareSum(9))

#juedgeSquareSum(2)
#import math
#class Solution:
#    def judgeSquareSum(c):
#        if c<=0:
#           return 'no solution'
#        r=int(math.sqrt(c))+1
#        for i in range(r):
#           m=c-i*i
#            if math.sqrt(m) in range(r):
#                return True
#            else:
#                continue
#        return False
    
#print(Solution.judgeSquareSum(6))
        
#juedgeSquareSum(3)
#import math
#class Solution:
#    def judgeSquareSum(c):
#        if c<=0:
#           return 'no solution'
#        r=int(math.sqrt(c))
#        i=0
#        j=r
#         while i<=j:
#            m=i*i+j*j
#            if m==c:
#                return True
#            elif m<c:
#                i+=1
#            else:
#                j-=1
#        return False
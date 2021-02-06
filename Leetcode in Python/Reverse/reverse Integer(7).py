#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 15:09:12 2021

@author: baoshiyuan
"""
###Way 1###
class Solution():
    def reverse(self,c):
        c_str=list(str(c))
        if c>=2**31-1 or c<=-2**31:
            return 0
        else:
            
            if c>=0: 
                a=[]
                for i in range(len(c_str)):
                    a.append(c_str[-(i+1)])
                    result=int("".join(a))
                    
            elif c<0:   
                a=[]
                for i in range(1,len(c_str)):
                    a.append(c_str[-i])  
                    result=-1*int("".join(a))
            if result>=2**31-1 or result<=-2**31:
                return 0
            else: return result
            
###Way 2###
#class Solution:
#    def reverse(self,n:int):
#        a=abs(n)
#        c=0
        
#        if n==0:
#           return n
        
#        while(a!=0):
#            b=a%10
#            c=c*10+b
#            a=a//10
            
        
#       if n>0 and c<=2**31-1:
#            return c
#        elif n<0 and c<=2**31-1:
#            return -c
#        elif (n>0 and c>2**31-1) or (n<0 and c>2**31):
#           return 0            
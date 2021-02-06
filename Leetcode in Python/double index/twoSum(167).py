#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 13:00:06 2020

@author: baoshiyuan
"""


class Solution:
    def twoSum( nums, target):
       i=0
       j=len(nums)-1
        while i<len(nums)-1:
            if i==len(nums)-1:
                return 'no solution'
            while i<j:
                sum=nums[i]+nums[j]
                if sum<target:
                    i+=1
                elif sum> target:
                    j-=1
                else:
                    return [i,j]
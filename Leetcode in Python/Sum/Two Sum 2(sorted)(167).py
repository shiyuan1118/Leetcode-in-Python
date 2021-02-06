#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 15:22:45 2021

@author: baoshiyuan
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        while i<j:
            value=numbers[i]+numbers[j]
            if value<target:
                i+=1
            elif value>target:
                j-=1
            else:
                return[i+1,j+1]
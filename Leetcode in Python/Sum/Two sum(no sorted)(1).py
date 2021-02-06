#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 15:17:08 2021

@author: baoshiyuan
"""

###Way 1###
class Solution:
    def twoSum(self,nums,target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]

###Way 2###
#class Solution:
#    def twoSum(self, nums, target):
#        i = 0
#        while i < len(nums):
#            if i == len(nums) - 1:
#                return "No solution here!"
#            r = target - nums[i]
            # Can't use a num twice
#            num_follow = nums[i + 1:]
#            if r in num_follow:
#                return [i, num_follow.index(r) + i + 1]
#            i = i + 1                    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 15:27:33 2021

@author: baoshiyuan
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        result=[]
        
        for i in range(n-2):
            if nums[i]+nums[i+1]+nums[i+2]>0:
                break
            if nums[i]+nums[n-1]+nums[n-2]<0:
                continue
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            l=i+1
            r=n-1
            while l<r:
                temp=nums[i]+nums[l]+nums[r]
                if temp==0:
                    result.append([nums[i],nums[l],nums[r]])
                    while l+1<r and nums[l]==nums[l+1]:
                        l+=1
                    l+=1
                    while r-1>l and nums[r]==nums[r-1]:
                        r-=1
                    r-=1
                elif temp>0:
                    r-=1
                else:
                    l+=1
        return result
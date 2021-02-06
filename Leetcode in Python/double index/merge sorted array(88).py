#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 13:09:50 2020

@author: baoshiyuan
"""

#Merge Sorted Array
class Solution:
    def merge(nums1, m, nums2, n):
   
        while m>0 and n>0:
            if nums2[n-1]>nums1[m-1]:                
                nums1[m+n-1]=nums2[n-1]
                n=n-1
            else:
                nums1[m-1],nums1[m+n-1]=nums2[n-1],nums1[m-1]
                m=m-1
        if m==0 and n>0:
            nums1[:n]=nums2[:n]##if the length of nums2 is greater than nums1,then put the rest of nums2 in the front of merger
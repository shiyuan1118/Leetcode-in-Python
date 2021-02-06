#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 20:31:38 2021

@author: baoshiyuan
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        new=dummy=ListNode(0)
        
        while l1 and l2:
            if l1.val < l2.val:
                new.next=l1
                l1=l1.next
            else:
                new.next=l2
                l2=l2.next
            new=new.next
        
        new.next=l1 or l2
        
        return dummy.next
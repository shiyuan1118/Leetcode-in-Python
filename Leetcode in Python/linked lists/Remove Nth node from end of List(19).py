#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 21:22:10 2021

@author: baoshiyuan
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy=ListNode(0)
        dummy.next=head
        fast=slow=dummy
        
        for _ in range(n):
            fast=fast.next
        
        while fast.next:
            slow=slow.next
            fast=fast.next
        
        slow.next=slow.next.next
        
        return dummy.next
        
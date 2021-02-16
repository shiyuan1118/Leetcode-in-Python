#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 10:49:53 2021

@author: baoshiyuan
"""

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy=ListNode(0)
        dummy.next=head
        pre, curr = dummy, dummy.next
        while curr:
            if curr.val==val:
                pre.next=curr.next
            else:
                pre=curr
            curr=curr.next
        
        return dummy.next
        
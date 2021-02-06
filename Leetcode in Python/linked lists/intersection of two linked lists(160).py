#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 19:30:47 2020

@author: baoshiyuan
"""

class ListNode:
     def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(headA: ListNode, headB: ListNode):
        p1=headA
        p2=headB
        
        while p1!=p2:
            if not p1:
                p1=headB
            else:
                p1=p1.next
            if not p2:
                p2=headA
            else:
                p2=p2.next
        return p2
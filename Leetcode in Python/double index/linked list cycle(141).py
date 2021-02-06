#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 11:17:31 2020

@author: baoshiyuan
"""

#linked list cycle
class ListNode:
     def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle( head):
        
        fast,slow = head, head        
        while fast and fast.next:
            fast, slow= fast.next.next, slow.next
            if fast == slow:
                return True
        return False
    
            
        
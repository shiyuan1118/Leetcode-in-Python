#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 17:12:54 2021

@author: baoshiyuan
"""

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        newhead=ListNode(float("-inf"))
               
        while head:
            newhead.next, head.next, head = head, newhead.next, head.next
        return newhead.next
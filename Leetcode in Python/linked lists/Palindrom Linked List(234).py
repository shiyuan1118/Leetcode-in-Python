#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 21:11:43 2021

@author: baoshiyuan
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
###Way1###
#class Solution:
#    def isPalindrome(self, head: ListNode) -> bool:
#        fast=slow=ListNode(0)
#        fast=slow=head
#        stack=[]
        
#        while fast and fast.next:
#            stack.append(slow.val)
#            fast=fast.next.next
#            slow=slow.next
        
#        if fast:
#            slow=slow.next
        
#        while slow:
#            top=stack.pop()
#            if top!=slow.val:
#                return False
#            else:
#                slow=slow.next
#        return True
    
    
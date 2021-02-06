#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 21:52:50 2021

@author: baoshiyuan
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1==None:
            return l2
        if l2==None:
            return l1
        
        carry=0
        dummy=ListNode(0)
        p=dummy
        
        carry=0
        while l1 and l2:
            mod=(l1.val+l2.val+carry)%10
            carry=(l1.val+l2.val+carry)//10
            p.next=ListNode(mod)
            l1=l1.next
            l2=l2.next
            p=p.next
        
        if l1:
            while l1:
                p.next=ListNode((l1.val+carry)%10)
                carry=(l1.val+carry)//10
                l1=l1.next
                p=p.next
        
        if l2:
            while l2:
                p.next=ListNode((l2.val+carry)%10)
                carry=(l2.val+carry)//10
                l2=l2.next
                p=p.next
        
        if carry==1:
            p.next=ListNode(1)
            
        return dummy.next
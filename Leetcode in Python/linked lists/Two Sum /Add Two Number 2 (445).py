#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 18:16:17 2021

@author: baoshiyuan
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1=[]
        stack2=[]
             
        
        def push_stack(p,stack):
            while p:
                stack.append(p.val)
                p=p.next
    
        push_stack(l1,stack1)
        push_stack(l2,stack2)
    
        answer=None
        carry = 0
        while stack1 or stack2 or carry:
            tmp1,tmp2=0,0
            if stack1:
                tmp1=stack1.pop()
            if stack2:
                tmp2=stack2.pop()
            
            mod=(tmp1+tmp2+carry)%10
            carry=(tmp1+tmp2+carry)//10
        
            tmp=answer
            answer=ListNode(mod)
            answer.next=tmp
    
        return answer
        
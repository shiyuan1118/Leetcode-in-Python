#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 21:21:55 2021

@author: baoshiyuan
"""

class Solution:
    def reverseBits( n: int):
        str="{0:032b}".format(n)
        reversed=str[::-1]
        return int(reversed,2)


        
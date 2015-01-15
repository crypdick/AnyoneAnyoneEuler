# -*- coding: utf-8 -*-
"""
Problem 6 - Sum square difference

Created on Thu Jan 15 00:16:07 2015
@author: Richard Decal, decal@uw.edu
"""

x = sum(range(1,101)) ** 2  - sum([x**2 for x in range(1,101)])
print x

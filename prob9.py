#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 21:42:12 2019

@author: harineem
"""
'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.'''
'''       a = m2 - n2
       b = 2 * m * n
       c  = m2 + n2
because,
       a2 = m4 + n4 – 2 * m2 * n2
       b2 = 4 * m2 * n2
       c2 = m4 + n4 + 2* m2 * n2
a + b + c = m**2-n**2 +2*m*n +m**2 - n**2
Hence a+b+c=2m**2 +2mn = 1000
so a+b+c = 2m(m+n) = 1000
m(m+n) = 1000
'''
import math
num = 500
ltfact =math.sqrt(num)
# find all factors of 500
fact = list()
for i in range(2,int(ltfact) ):
    rem = num%i
    if(rem==0):
        m = i
        quot = num//i
        n = quot-m
        if(m>n):
           
            # check if it is a triplet
            a =(m**2-n**2)
            b = (2*m*n)
            c =(m**2+n**2)
            z = a+b+c
            csq = a**2+b**2
            if(z==1000 and (c**2==csq)) :
                y = a*b*c
                print(y)
                exit





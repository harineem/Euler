#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 15:37:08 2019

@author: harineem
"""
'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

'''
import math
def isPrime(n) :
    #if(n==2 or n==3 or n==5 or n==7 or n==11): return True
    if(n%2==0 or n%3==0 or n%5==0 or n%7==0 or n%11==0 or n%13==0 or n%17==0 or n%19==0 or n%23==0 or n%29==0): return False
    x = int(math.sqrt(n));
    divisors = [k for k in range(29,x) if (k%2!=0 and k%3!=0 and k%5!=0 and k%7!=0 and k%11!=0 and k%13!=0 and k%17!=0 and k%19!=0 and k%23!=0  and k%29!=0  )] 
    for k in range(29,x+1):
        if(n%k==0): return False
    return True



lt =10001


st = 31
cnt = 11
prime = st
while cnt<lt:
    st = st +1
  
    if(isPrime(st)) :
       cnt = cnt +1
 
       prime = st
print(cnt)
print(prime)

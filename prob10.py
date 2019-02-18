#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 12:01:48 2019

@author: harineem
"""

'''

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.'''

def isPrime(n) :
    #if(n==2 or n==3 or n==5 or n==7 or n==11): return True
    #if(n%2==0 or n%3==0 or n%5==0 or n%7==0 or n%11==0 or n%13==0 or n%17==0): return False
    x = int(math.sqrt(n));
    divisors = [k for k in range(37,x) if (k%2!=0 and k%3!=0 and k%5!=0 and k%7!=0 and k%11!=0 and k%13!=0 and k%17!=0 and k%19!=0 and k%23!=0 and k%29!=0 and k%31!=0)] 
    for k in range(37,x+1):
        if(n%k==0): return False
    return True

sumn = 2+3+5+7+11+13+17+19+23+29+31 
#nums = list(range(19,1999999))
#x = list(filter(lambda num : isPrime(num)==True, nums))
#y5 = [k for k in range(25,2000000,5)]
#y3 = [k for k in range(24,2000000,3)]
lt =2000000

y = [ k for k in range(37,lt) if (k%2!=0 and k%3!=0 and k%5!=0 and k%7!=0 and k%11!=0 and k%13!=0 and k%17!=0 and k%19!=0 and k%23!=0 and k%29!=0 and k%31!=0 )]

for i in y :
   
    j =i
    if(isPrime(i)) :
        #code adding
        
        j =j*i
        while(j<lt):
            y.remove(j)
            j = j*i
#
        sumn = sumn +i
       
print(sumn)



__author__ = 'harineem'
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
import math

def isPrime(n) :
    if(n==2 or n==3 or n==5 or n==7 or n==11): return True
    if(n%2==0 or n%3==0 or n%5==0 or n%7==0 or n%10==0): return False
    x = int(n/2);
    for k in range(11,x,1):
        if(n%k==0): return False
    return True


n = 600851475143
#n = 13195
m = int(math.sqrt(n))
prfactor =1
for k in range(m,2,-1) :
    if n%k==0 and isPrime(k) :
        prfactor = k
        break


print(prfactor)





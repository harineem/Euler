__author__ = 'harineem'
#2520 is the smallest number that can be divided by each of the numbers 
#from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def isPrime(n) :
    if(n==2 or n==3 or n==5 or n==7 or n==11): return True
    if(n%2==0 or n%3==0 or n%5==0 or n%7==0 or n%10==0): return False
    x = int(n/2);
    for k in range(11,x,1):
        if(n%k==0): return False
    return True
n=20
prod = 1
for k in range(2,n+1) :
    if isPrime(k) :
        j=k
        while True:
           # print("k " + str(k))
            #print("j " + str(j))
            if (j*k)<=n :
                j = j*k
            else:
                break
        prod = prod*j
        #print("==="+str(prod1))

print(prod)

#4,5,6,7,8,9
__author__ = 'harineem'
#A palindromic number reads the same both ways. 
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.
#Largest palindrome product
def isPalindrome(num) :
    
    s = str(num)
    if(s==s[::-1]) :
        return True
    else:
        return False

def findmaxpal(n):
    for k in range(n-1,int(n/10)+1,-1):
        for j in range(n-1,int(n/10)+1,-1):
            x = k*j
            if x%10==0 : break
            if(isPalindrome(x)) :
                print(" Numbers " +str(k) + "  "+str(j))
                return x
n =1000
print(findmaxpal(n))




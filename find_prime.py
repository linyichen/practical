# find prime.py
# to find the nth prime number efficiently

import math

def is_prime(k):
        if k ==2:
            return True
        elif k % 2 ==0:
            return False
        else:
            temp = int(math.sqrt(k))+1
            for i in range (3, temp, 2):
                if k % i == 0:
                    return False
        return True
    
# main
# get input n 
n = int(input("Enter n: "))

# find nth prime number
count = 1 #number of primes so far
num = 1 #starting number to test for primality 
if n == 1:
    num = 2
else:
    while count < n:
        num = num + 2
        if is_prime(num):
            count = count + 1
            
# display result
print (num)

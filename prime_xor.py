# Run in pypy3

import math
import os
import random
import re
import sys
from collections import Counter #Import counter to count the number of occurance of elements

def is_prime(x):       #Takes in an element and checks if it is a prime or not. Time complexity O(sqrt(n))
    if x <= 1:          #Base conditions 
        return False    # 1 and 0 is not a prime
    if x <= 3:          
        return True     # 2 and 3 are prime
    if (x%2 == 0 or x%3 == 0):  # any number divisible by 2 or 3 is not a prime
        return False            # This completes all numbers till 25
    i = 5
    while(i*i <= x):        
        if (x%i == 0 or x%(i+2) == 0):      # Every integer can be represented as (6i+n) where n = [0,1,2,3,4,5]
            return False                # In which every prime can be represented as (6i+1) or (6i+5)[also represented 
            # as (6i-1)]
        i += 6      
    return True         # Returns True for prime and False for not prime

def primeXor(a):
    MOD = (10**9)+7
    count = 0
    c = Counter(a)      # Keep count on elements 
    Max = 8192          # 2^13 (8192) is the max attained xor value for i in range 3500 and 4500
        
    dp = [0] * Max      # Initilizes dynamic programming array
    dp[0] = 1           # Setting first element to 1
    for e in c.keys():  
        even, odd = (c[e]//2 + 1), ((c[e] + 1)//2)      # For even occurances the xor will be same as no occurance and for 
        # all odd occurance it can be represented as 1 occurance.
        # e.g., for {5,5,5,7} Counter c = {(5:3),(7,1)}
        # Possiblities of 5 occuring are [0,1,2,3]
        # For 0 and 2 the result is same (Even occurance = 2) as the two 5s cancels each other.
        # And for 1 and 3 the result will be (Odd occurance = 2) as the odd number of occurance will retail the number iteslef 
        dp = [(dp[i] * even + dp[i^e] * odd) % MOD for i in range(Max)]
        # Dynamically changing the dp array such that all possible xor combinations is counted
    for j in range(Max):
        if is_prime(j): 
            count += dp[j]  # The count is only added to the return value only if the index is a prime (ie the xor value is a prime)
            if count > MOD:
                count %= MOD # Count is normalized
    return count

if __name__ == '__main__':
    q = int(input())  # Input Number of testcases
    result = []
    for q_itr in range(q):
        n = int(input())    # Input array length for each testcase
        a = list(map(int, input().rstrip().split()))    # Input the array
        result.append(primeXor(a)) 
    for res in result:
        print(res)

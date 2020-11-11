# HackerRank Solutions
This repo contains some hackerrank solutions that have a `Medium` difficulty in python.

# Problems.. 
## Megaprime
Link: https://www.hackerrank.com/contests/w29/challenges/megaprime-numbers/problem
The basic logic of the solution is to create all the `megaprimes` in the given range. 
According to the constraints a megaprime should only be consist of `[2,3,5,7]`. Thus we can create any `megaprime` in the given range with an entropy of `9` without breaking the time barrier. As said in the constraints ```last - first <= 10^9```. 
To confirm primality millers primality test is used.
## Almost sorted
Link: https://www.hackerrank.com/challenges/almost-sorted/problem
The idea is to iterate over the length of the array checking wheather any character is misplaced. If any adding index to a list and add the value to another list. If the length of the index list is `2` then we can swap those elements to get the sorted array. If the length is not 2 then we have to check if the sorted version of the value array and the reversed version of value array are equal. If equal then we can apply reverse. Else print `no`.
## Ways to give check
Link: https://www.hackerrank.com/contests/w36/challenges/ways-to-give-a-check
Any one with basic programming skills and patience can solve this problem. The idea is to hardcode every possible scenerio of the checks and add the count. Since the array is always `8*8` there is no problem of time complexity.
## Connected cells in a grid
Link: https://www.hackerrank.com/challenges/connected-cell-in-a-grid/problem
The solution for this problem is to implement `flood-fill` algorithm.
## Prime XOR
Link: https://www.hackerrank.com/challenges/prime-xor/problem
This problem requires some pre-requsit knowledge on dynamic programming. The straight forward solution is to find every subset and calculate its XOR value. But it is time consuming. The other is the dp approach. Make a dp array and update the array with each step. Then check whether the index of array is prime and add the count.
## Candles counting
Link: https://www.hackerrank.com/challenges/candles-2/problem
The problem uses dp, fenwick tree/binary indexed tree, inclusion-exclusion principle, and bitmasking.



### Note
If you can provide solutions for any hackerrank problems, add it and update this README and open a pull request.

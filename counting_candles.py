# Run in Pypy3          Total time complexity - O(2^k n log n)

MOD = (10**9)+7 # Final Mod value

# The update and getsum functions are for Ferwicks tree or Binary Indexed tree. Time complexity is O(log n)
# These are used to find the sum till index i of a dynamically updating array. 
def update(BIT, q, x, m):
    while q < m:
        BIT[q] += x     # Adding sum to the parent nodes in a binary tree.
        q += q & (-q)    # Find the next parent node. The parent nodes will be [2,4,8,.....]
                        #  The parent nodes store the intermediate sum values.

def getsum(BIT, index):     # Find the sum of the array till and index (i)
    s = 0
    while index > 0:
        s += BIT[index]
        index -= index & (-index)   # Climbs along the parent nodes to find the sum.
    return s%MOD

def candlesCounting(k, heights, C):
    # The equation used is inclusion-exclusion principle. 
    # n(A n B n C) = n(A u B u C) - n(A) - n(B) - n(C) + n(A n B) + n(A n C) + n(B n C)
    
    m = max(heights)+1      # To create an array with size max value of heights
    result = 0
    c_pow = ((1 << k))      # This is same as 2**k
    # c_pow is the bit size of all the colors. Thus colors will be a k-bit value, where i-th bit is set to
    # know if C[i] is included in the subsequence or not.
    for color in range(1, c_pow):
        BIT = [0]*m         # Initilizing Binary Indexed Array for dynammic programming
        for j in range(n):
            # Consider cacndle j only if that bit is set to '1'
            # For 3 colors the bit size will be 8. 
            # All possible bit after masking will be [000, 001, 010, 011, 100, 101, 110, 111]
            # If i-th bit is '1' then that color is present in the subsequence.
            if((color >> (C[j] - 1)) & 1):
                # Number of strictly increasing in height subsequence ending with heights[i] = 1 + Sum of number of subsequence ending with [1,2,3,.....H[i] - 1]
                # Update BIT dynamically thus the array changes with each iteration.
                update(BIT, heights[j], (1 + getsum(BIT, heights[j]-1)), m)
        # Find number of strictly increasing subsequence that contain candles of any number of colors and add.
        if bin(color).count('1')%2 == k % 2:
            result += getsum(BIT, m-1)
            result %= MOD
        # Remove the increasing subsequence that do not contain candles of k colors.
        else:
            result -= getsum(BIT, m-1)
            result %= MOD
    return result

if __name__ == '__main__':
    nk = input().split()    # Take input n and k
    n = int(nk[0])
    k = int(nk[1])
    heights = []
    C = []
    for i in range(n):
        h,c=[int(d) for d in input().split(' ')]
        heights.append(h)   # Rather than appending to a single array appending to two arrays
        C.append(c)         # heights and colors(C).
    result = candlesCounting(k, heights, C)
    print(result)
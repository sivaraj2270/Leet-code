''' Mirror Distance of an Integer

Example 1:

Input: n = 25

Output: 27

Explanation:

reverse(25) = 52.
Thus, the answer is abs(25 - 52) = 27. '''

#code link : https://leetcode.com/problems/mirror-distance-of-an-integer/description/

class Solution:
    def mirrorDistance(self, n: int) -> int:
        a = str(n)[::-1]
        b = int(a)
        c = b - n 
        return abs(c)
      

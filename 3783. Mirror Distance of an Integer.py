'''3783. Mirror Distance of an Integer

Example 1:

Input: n = 25

Output: 27

Explanation:

reverse(25) = 52.
Thus, the answer is abs(25 - 52) = 27'''


#code link : https://leetcode.com/problems/mirror-distance-of-an-integer/

class Solution:
    def mirrorDistance(self, n: int) -> int:
        d = str(n)
        a = int(d[::-1])
        b = n - a
        return abs(b)

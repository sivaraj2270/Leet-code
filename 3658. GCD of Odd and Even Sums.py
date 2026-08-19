'''3658. GCD of Odd and Even Sums


Example 1:

Input: n = 4

Output: 4

Explanation:

Sum of the first 4 odd numbers sumOdd = 1 + 3 + 5 + 7 = 16
Sum of the first 4 even numbers sumEven = 2 + 4 + 6 + 8 = 20
Hence, GCD(sumOdd, sumEven) = GCD(16, 20) = 4.'''

#code link : https://leetcode.com/problems/gcd-of-odd-and-even-sums/

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd = 0
        even = 0
        a = n * 2
        for i in range(1, a):
            if i % 2 != 0:
                odd += i
            else:
                even += i
        return math.gcd(even, odd)

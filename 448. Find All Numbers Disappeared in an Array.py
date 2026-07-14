'''Find All Numbers Disappeared in an Array

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]'''

#code link : https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        count = []

        s = set(nums)

        for i in range(1, len(nums)+1):
            if i not in s:
                count.append(i)
        return count

'''412. Fizz Buzz

Example 1:

Input: n = 3
Output: ["1","2","Fizz"]'''


#code link : https://leetcode.com/problems/fizz-buzz/description/


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        count =[]

        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                count.append("FizzBuzz")
            elif i % 3 == 0:
                count.append("Fizz")
            elif i % 5 == 0:
                count.append("Buzz")
            else:
                count.append(str(i))
        return count
    

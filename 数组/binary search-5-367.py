# leetcode 367 有效的完全平方数
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num

        while left <= right:
            middle = left + (right - left) // 2
            if middle * middle < num:
                left = middle + 1
            elif middle * middle >num:
                right = middle -1
            else:
                return True
        return False
# leetcode 69 平方根计算
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x + 1

        while left <= right:
            middle = left + (right - left) // 2
            if middle * middle < x:
                left = middle +1
            elif middle *middle > x:
                right = middle -1
            else:
                return middle
        return right
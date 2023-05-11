# leetcode 35 搜索插入位置
class Solution:
    def search (self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1


        while left <= right:
            middle = left + (right - left) // 2  #防溢出

            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle -1
            else:
                return middle
        return right + 1
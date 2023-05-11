# leetcode 34 在排序数组中查找元素的第一个和最后一个位置
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
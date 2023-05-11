#有序数组的平方
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        size = len(nums)
        res = [0] * size
        k, left, right = size - 1, 0, size - 1
        while left <= right:
            if nums[left] * nums[left] > nums[right] * nums[right]:
                res[k] = nums[left] * nums[left]
                left += 1
            else:
                res[k] = nums[right] * nums[right]
                right -= 1
            k -= 1

        return res
#比较含退格的字符串
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow, fast = 0, 0
        size =len(nums)
        while fast < size:
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        while size - slow > 0:
            nums[slow] = 0
            slow += 1
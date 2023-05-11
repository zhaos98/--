#删除排序数组中的重复项
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        fast = 1
        size = len(nums)
        nums[slow] = nums[0]
        while fast < size:
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]

            fast += 1
        return slow + 1
#长度最小的子数组
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = float ("inf") #无穷大
        sum = 0
        i = 0
        for j in range(len(nums)):
            sum += nums[j]
            while(sum >= target):
                result = min(result , j - i +1)
                sum -= nums[i]
                i += 1
        return 0 if result == float("inf") else result
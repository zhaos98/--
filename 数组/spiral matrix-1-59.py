#螺旋矩阵Ⅱ
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        nums = [[0] * n for _ in range(n)]
        x, y = 0, 0
        loop, mid = n // 2, n // 2
        count = 1
        for offset in range(1, loop + 1):
            for i in range(y, n - offset):
                nums[x][i] = count
                count += 1
            for i in range(x, n-offset):
                nums[i][n - offset] = count
                count += 1
            for i in range(n - offset, y, -1):
                nums[n - offset][i] = count
                count += 1
            for i in range(n - offset, x, -1):
                nums[i][y] = count
                count += 1
            x += 1
            y += 1

        if n % 2 != 0:
            nums[mid][mid] = count
        return nums
#螺旋矩阵
#剑指offer第29题
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return list()

        res = []
        L, T = 0, 0
        R, B = len(matrix[0]) - 1, len(matrix) - 1
        sum = len(matrix[0]) * len(matrix)

        while sum >= 1:
            for i in range(L, R + 1):
                if sum >= 1:
                    res.append(matrix[T][i])
                    sum -= 1
            T += 1
            for i in range(T, B + 1):
                if sum >= 1:
                    res.append(matrix[i][R])
                    sum -= 1
            R -= 1
            for i in range(R, L - 1, -1):
                if sum >= 1:
                    res.append(matrix[B][i])
                    sum -= 1
            B -= 1
            for i in range(B, T - 1, -1):
                if sum >= 1:
                    res.append(matrix[i][L])
                    sum -= 1
            L += 1
        return res

s = Solution()
nums = s.spiralOrder([[3],[2]])
print(nums)
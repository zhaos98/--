#水果成篮
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        i, j = 0, 0
        res = 0
        classMap = defaultdict(int)
        classcnt = 0

        while j < len(fruits):
            if classMap[fruits[j]] == 0:
                classcnt += 1
            classMap[fruits[j]] += 1

            while classcnt > 2:
                if classMap[fruits[i]] == 1:
                    classcnt -= 1
                classMap[fruits[i]] -= 1
                i += 1

            res = max(res, j - i + 1)
            j += 1
        return res
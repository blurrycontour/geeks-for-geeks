# https://practice.geeksforgeeks.org/problems/lucky-numbers2911/1

class Solution:
    def isLucky(self, n):
        numbers = list(range(1,n+1))
        i = 2
        while len(numbers) >= i:
            del numbers[i-1::i]
            i += 1
            if n not in numbers:
                return False
        return True


if __name__ == "__main__":
    cases = [
        5, # 0
        19, # 1
    ]

    for c in cases:
        obj = Solution()
        if obj.isLucky(c):
            print(1)
        else:
            print(0)

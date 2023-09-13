# https://practice.geeksforgeeks.org/problems/largest-number-possible5028/1

class Solution:
    def findLargest(self, N, S):
        if S == 0 and N != 1:
            return -1
        number = 0
        for _ in range(1,N+1):
            d = 0
            if S > 9:
                d = 9
            else:
                d = S
            number = number * 10 + d
            S -= d
        if S != 0:
            return -1
        return number


if __name__ == "__main__":
    cases = [
        (2,9), # 90
        (3,20), # 992
        (2,5), # 50
        (1,0), # 0
        (4,0), # -1
        (1,15), # -1
    ]

    for c in cases:
        obj = Solution()
        print(obj.findLargest(*c))

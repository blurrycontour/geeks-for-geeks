# https://practice.geeksforgeeks.org/problems/multiply-two-strings/1

class Solution:
    def multiplyStrings(self,s1,s2):
        nums = ()
        for s in (s1,s2):
            n = 0
            for i, d in enumerate(s[::-1]):
                if d != "-":
                    n += (ord(d)-48) * 10**i
                else:
                    n *= -1
            nums += (n,)
        return nums[0]*nums[1]


if __name__ == "__main__":
    s = Solution()
    print(s.multiplyStrings("0033", "2")) # 66
    print(s.multiplyStrings("-0033", "2")) # -66
    print(s.multiplyStrings("-0033", "-002")) # 66
    print(s.multiplyStrings("11","23")) # 253

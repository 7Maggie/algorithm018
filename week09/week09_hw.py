# 91. 解码方法
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        dp = [0]*(n+1)
        dp[0] = 1
        for i in range(1,n+1):
            t = int(s[i-1])
            # 最后一个字母由最后一个数字解密得到
            if t >= 1 and t <= 9:
                dp[i] += dp[i-1]
            # 最后一个字母由最后两个数字解密得到
            if i >= 2:
                t = int(s[i-2]) * 10 + int(s[i-1])
                if t >= 10 and t <= 26:
                    dp[i] += dp[i-2]
        return dp[-1]
# 5. 最长回文子串
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        # dp[i][j]表示字符串s的第i个字符到第j个字符是否为回文子串
        dp = [[False] * n for i in range(n)]
        res = ''
        # 枚举子串的长度为size+1
        for size in range(n):
            for i in range(n):
                j = i + size
                # 特殊情况，超出长度
                if j >= n:
                    break
                # 特殊情况：当子串长度为1时，是回文子串
                if size == 0:
                    dp[i][j] = True
                # 特殊情况：当子串长度为2时，两个字符相同，则为回文串
                elif size == 1:
                    dp[i][j] = (s[i]==s[j])
                # 回文串子串，头尾添上相同的字符，仍为回文串
                else:
                    dp[i][j] = (dp[i+1][j-1] and s[i] == s[j])
                # 找到最长的回文子串
                if dp[i][j] and size + 1 > len(res):
                    res = s[i:j+1]
        return res
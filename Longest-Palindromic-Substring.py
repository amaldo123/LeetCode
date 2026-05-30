1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        longest = ""
4
5        def expand(left, right):
6            while left >= 0 and right < len(s) and s[left] == s[right]:
7                left -= 1
8                right += 1
9            return s[left + 1:right]
10
11        for i in range(len(s)):
12            p1 = expand(i, i)       # odd length
13            p2 = expand(i, i + 1)   # even length
14
15            if len(p1) > len(longest):
16                longest = p1
17
18            if len(p2) > len(longest):
19                longest = p2
20
21        return longest
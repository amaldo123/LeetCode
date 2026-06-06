1class Solution:
2    def isMatch(self, s: str, p: str) -> bool:
3        m, n = len(s), len(p)
4        
5        # dp[i][j] represents if s[:i] matches p[:j]
6        dp = [[False] * (n + 1) for _ in range(m + 1)]
7        
8        # Empty string matches empty pattern
9        dp[0][0] = True
10        
11        # Handle patterns like a*, a*b*, a*b*c* that can match empty string
12        for j in range(2, n + 1):
13            if p[j-1] == '*':
14                dp[0][j] = dp[0][j-2]
15        
16        # Fill the DP table
17        for i in range(1, m + 1):
18            for j in range(1, n + 1):
19                if p[j-1] == '*':
20                    # Match zero times: skip the pattern a*
21                    dp[i][j] = dp[i][j-2]
22                    
23                    # Match one or more times: current char matches pattern's preceding char
24                    # and the previous part matches
25                    if p[j-2] == '.' or p[j-2] == s[i-1]:
26                        dp[i][j] = dp[i][j] or dp[i-1][j]
27                else:
28                    # Normal character or '.'
29                    if p[j-1] == '.' or p[j-1] == s[i-1]:
30                        dp[i][j] = dp[i-1][j-1]
31        
32        return dp[m][n]
1class Solution:
2    def longestCommonPrefix(self, strs: list[str]) -> str:
3        i = 0
4
5        while i < len(strs[0]):
6             for j in range(1, len(strs)):
7                 if i >= len(strs[j]) or strs[j][i] != strs[j-1][i]:
8                   return strs[0][:i]
9             i += 1
10
11        return strs[0]
12       
13        
14         
15          
16        
17        
18       
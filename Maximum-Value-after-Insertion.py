1class Solution:
2    def maxValue(self, n: str, x: int) -> str:
3        l = len(n)
4        if n[0] == "-":
5         
6         for i in range(1,l):
7            if x < int(n[i]):
8                
9                return n[:i] + str(x) + n[i:]
10         return n + str(x)  
11        else:
12         for i in range (l) :
13            if str(x) > n[i]:
14                t = i-1
15                return n[:i] + str(x) + n[i:]
16
17         return n + str(x)
18
19    
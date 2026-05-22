1class Solution:
2    def reverse(self, x: int) -> int:
3        t = str(x)
4        s = list(t)
5        l = len(s)
6        mid = int(l/2)
7        if str(s[0]) == "-":
8            for i in range(1,int((l+1)/2)):
9            
10                temp = s[i]
11                s[i] = s[l-i]
12                s[l-i] = temp
13        else:
14            for i in range(mid):
15            
16                temp = s[i]
17                s[i] = s[l-1-i]
18                s[l-1-i] = temp
19        r = "".join(s)
20        if int(r) < (2**31) - 1 and int(r) > (-2)**31 :
21            return int(r)
22        else:
23            return 0
24
25         
26        
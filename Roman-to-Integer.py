1class Solution:
2    def romanToInt(self, s: str) -> int:
3        roman = {
4            'I': 1,
5            'V': 5,
6            'X': 10,
7            'L': 50,
8            'C': 100,
9            'D': 500,
10            'M': 1000
11        }
12        
13        total = 0
14        
15        for i in range(len(s) - 1):
16            # If current value < next value, subtract it
17            if roman[s[i]] < roman[s[i + 1]]:
18                total -= roman[s[i]]
19            else:
20                total += roman[s[i]]
21        
22        # Always add the last symbol
23        total += roman[s[-1]]
24        
25        return total
26
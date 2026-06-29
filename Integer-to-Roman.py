1class Solution:
2    def intToRoman(self, num: int) -> str:
3        
4        numstr = str(num)
5        
6        numarr = list(numstr)
7        numarr.reverse()
8        
9        final = []
10        i = 0
11        for num in numarr:
12            
13            num = int(num)
14            if i == 0:
15                if num == 4:
16                    final.append("IV")
17                elif num == 9:
18                    final.append("IX")
19                elif num >= 1 and num < 4:
20                    prep = "I"*num
21                    final.append(prep)
22                elif num >= 5 and num < 9:
23                    prep = "V" + "I"* (num - 5)
24                    final.append(prep)
25            if i == 1:
26                if num == 4:
27                    final.append("XL")
28                elif num == 9:
29                    final.append("XC")
30                elif num >= 1 and num < 4:
31                    prep = "X"*num
32                    final.append(prep)
33                elif num >= 5 and num < 9:
34                    prep = "L" + "X"* (num - 5)
35                    final.append(prep)
36            if i == 2:
37                if num == 4:
38                    final.append("CD")
39                elif num == 9:
40                    final.append("CM")
41                elif num >= 1 and num < 4:
42                    prep = "C"*num
43                    final.append(prep)
44                elif num >= 5 and num < 9:
45                    prep = "D" + "C"* (num - 5)
46                    final.append(prep)
47            if i == 3:
48                    prep = "M"*num
49                    final.append(prep)
50            i += 1   
51        final.reverse()
52        result = "".join(final)
53        return result
54            
55
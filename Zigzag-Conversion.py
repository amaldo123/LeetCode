1class Solution:
2    def convert(self, s: str, numRows: int) -> str:
3        if numRows == 1 or numRows >= len(s):
4            return s
5
6        rows = [""] * numRows
7
8        current_row = 0
9        direction = 1   # 1 = down, -1 = up
10
11        for ch in s:
12            rows[current_row] += ch
13
14            # Change direction at top/bottom
15            if current_row == 0:
16                direction = 1
17            elif current_row == numRows - 1:
18                direction = -1
19
20            current_row += direction
21
22        return "".join(rows)
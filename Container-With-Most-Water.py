1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        left = 0
4        right = len(height) - 1
5        max_area = 0
6
7        while left < right:
8            width = right - left
9            area = min(height[left], height[right]) * width
10            max_area = max(max_area, area)
11
12            if height[left] < height[right]:
13                left += 1
14            else:
15                right -= 1
16
17        return max_area
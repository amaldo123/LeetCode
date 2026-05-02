1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        seen = {}
4        for i, num in enumerate(nums):
5            complement = target - num
6            if complement in seen:
7                return[seen[complement],i]
8                
9            seen[num] = i
10
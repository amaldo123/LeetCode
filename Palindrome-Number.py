1class Solution:
2    def isPalindrome(self, x: int) -> bool:
3        if x < 0:
4            return False
5        
6        s = str(x)
7        return s == s[::-1]
8
1class Solution:
2    def findMedianSortedArrays(self, nums1, nums2):
3        
4        # Make sure nums1 is the smaller array
5        if len(nums1) > len(nums2):
6            nums1, nums2 = nums2, nums1
7
8        x = len(nums1)
9        y = len(nums2)
10
11        low = 0
12        high = x
13
14        while low <= high:
15
16            partitionX = (low + high) // 2
17            partitionY = (x + y + 1) // 2 - partitionX
18
19            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
20            minRightX = float('inf') if partitionX == x else nums1[partitionX]
21
22            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
23            minRightY = float('inf') if partitionY == y else nums2[partitionY]
24
25            # Correct partition found
26            if maxLeftX <= minRightY and maxLeftY <= minRightX:
27
28                # Even total length
29                if (x + y) % 2 == 0:
30                    return (
31                        max(maxLeftX, maxLeftY) +
32                        min(minRightX, minRightY)
33                    ) / 2
34
35                # Odd total length
36                else:
37                    return max(maxLeftX, maxLeftY)
38
39            # Move left
40            elif maxLeftX > minRightY:
41                high = partitionX - 1
42
43            # Move right
44            else:
45                low = partitionX + 1
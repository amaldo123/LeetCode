1# Definition for singly-linked list.
2class ListNode:
3    def __init__(self, val=0, next=None):
4        self.val = val
5        self.next = next
6
7class Solution:
8    def insertionSortList(self, head):
9        dummy = ListNode(0)   # Start of sorted list
10        current = head
11
12        while current:
13            # Save next node
14            next_node = current.next
15
16            # Find insertion position
17            prev = dummy
18            while prev.next and prev.next.val < current.val:
19                prev = prev.next
20
21            # Insert current node
22            current.next = prev.next
23            prev.next = current
24
25            # Move to next node
26            current = next_node
27
28        return dummy.next
1
2
3class Solution:
4    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
5        dummy = ListNode()  # Dummy node to build the result list
6        current = dummy
7        carry = 0
8
9        # Loop through both lists and carry
10        while l1 or l2 or carry:
11            val1 = l1.val if l1 else 0
12            val2 = l2.val if l2 else 0
13
14            total = val1 + val2 + carry
15            carry = total // 10
16            digit = total % 10
17
18            current.next = ListNode(digit)
19            current = current.next
20
21            if l1:
22                l1 = l1.next
23            if l2:
24                l2 = l2.next
25
26        return dummy.next
27
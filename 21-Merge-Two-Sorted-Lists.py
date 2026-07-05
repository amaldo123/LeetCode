# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        final = ListNode()
        traverse = final
        while list1 or list2:
            if list1 and list2 and list1.val <= list2.val:
                newList1 = ListNode(list1.val)
                traverse.next = newList1
                traverse = traverse.next
                list1 = list1.next
            elif list2 and list1 and list2.val <= list1.val:
                newList2 = ListNode(list2.val)
                traverse.next = newList2
                traverse = traverse.next
                list2 = list2.next
            elif list1 and not list2:
                traverse.next = list1
                return final.next
            elif list2 and not list1:
                traverse.next = list2 
                return final.next

        return final.next
# 环形链表Ⅱ
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                index1 = head
                index2 = slow
                while index1 != index2:
                    index1 = index1.next
                    index2 = index2.next
                return index2
        return None

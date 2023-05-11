# 删除链表倒数第N个节点
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_node = ListNode(next = head)
        slow, fast = dummy_node, dummy_node
        while(n >= 0):
            fast = fast.next
            n -= 1
        while(fast != None):
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy_node.next
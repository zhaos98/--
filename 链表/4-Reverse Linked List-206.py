# 反转链表
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
##双指针法
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        pre = None
        while(cur != None):
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre

#递归法
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(pre, cur):
            if not cur:
                return pre
            temp = cur.next
            cur.next = pre
            return reverse(cur, temp)
        return reverse(None, head)
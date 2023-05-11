# 链表相交
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA, lenB = 0, 0
        cur = headA
        while cur:
            cur = cur.next
            lenA += 1
        cur = headB
        while cur:
            cur = cur.next
            lenB += 1
        curA, curB = headA, headB
        if lenA > lenB:
            curA, curB = curB, curA
            lenA, lenB = lenB, lenA
        for _ in range(lenB - lenA):
            curB = curB.next
        while curA:
            if curA == curB:
                return curA
            else:
                curA = curA.next
                curB = curB.next
        return None

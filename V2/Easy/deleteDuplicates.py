class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        LN = head
        while head != None:
            head = head.next
            if head != None:
                if LN.val != head.val:
                    LN.next = head
                    LN = LN.next
        return LN

LN = ListNode()
LN.val = 1
LN.next.val = 1
LN.next.next.val = 2
sol = Solution()
sol.deleteDuplicates(LN)

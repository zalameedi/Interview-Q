# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def insert(self, data):
        node = self
        while node != None:
            if node == None:
                node = ListNode(data)
            node = node.next
            

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        purge = self.getDuplicates(head)
        L = ListNode(0)
        for x in purge.keys():
            if purge[x] == 1:
                L.insert(purge[x])
        return L
        
    def getDuplicates(self,head):
        my_dict = {}
        temp = head.val
        while head != None:
            if head != None:
                try:
                    my_dict[(head.val)] += 1
                except KeyError:
                    my_dict[head.val] = 1
                temp=head.val
            head = head.next
        return my_dict

"[1,2,3,3,4,4,5]"
sol = Solution()
L = ListNode(1)
L.next=ListNode(2)
L.next.next=ListNode(3)
L.next.next.next=ListNode(3)
sol.deleteDuplicates(L)
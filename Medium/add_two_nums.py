# Definition for singly-linked list.
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head=head
    
    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

s1= ""
s2 = ""

class Solution:
    def rev_list(self, l1, l2):
        global s1
        global s2
        if l1 == None and l2 == None:
            return 
        else:
            self.rev_list(l1.next, l2.next)
            s1 += str(l1.val)
            s2 += str(l2.val)
    
    def print(self, l1):
        if l1 == None:
            return 
        else:
            self.print(l1.next)
            print(l1.val)
        
    def new_list_node(self, l, res3):
        for x in res3:
            if l == None:
                l = ListNode(int(x))
            else:
                while l != None:
                    l = l.next
                l = ListNode(int(x))

                            
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        global s1
        global s2
        self.rev_list(l1, l2)
        res1 = int(s1) + int(s2)
        res2 = list(str(res1))
        self.new_list_node(l1, res2)
        return l1

"""
[2,4,3]
[5,6,4]

"""

sol = Solution()
L1 = LinkedList(2)
L1.insert(4)
L1.insert(3)
L2 = LinkedList(5)
L2.insert(6)
L2.insert(4)
print(sol.addTwoNumbers(L1, L2))
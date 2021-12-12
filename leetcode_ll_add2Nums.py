# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SLinkedList:
   def __init__(self):
      self.headval = None

   def listprint(self):
      printval = self.headval
      while printval is not None:
         print (printval.val)
         printval = printval.next

list = SLinkedList()
list.headval = ListNode(1)
e2 = ListNode(2)
e3 = ListNode(3)

# Link first Node to second node
list.headval.next = e2

# Link second Node to third node
e2.next = e3

list.listprint()



#class Solution:
   # def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
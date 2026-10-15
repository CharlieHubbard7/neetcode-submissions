# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        start = list1
        while not (list1 == None and list2 == None): #list1.next != None and list2.next != None
                #find the lowest of the two, and put it on my current one. 
            if list2 != None and (list1 == None or list2.val < list1.val):
                list2nxt = list2.next
                newNode = ListNode(list2.val, list1)
                if previous != None:
                    previous.next = newNode
                else:
                    start = newNode
                previous = newNode
                list2 = list2nxt
            elif (list1 != None or list2.val >= list1.val):
                previous = list1
                list1 = list1.next
        return start
            
        
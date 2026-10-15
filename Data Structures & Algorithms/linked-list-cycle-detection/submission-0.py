# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        rabbit = head
        turtle = head
        while (rabbit != None and rabbit.next != None):
            turtle = turtle.next
            rabbit = rabbit.next.next
            if turtle == rabbit:
                return True
        return False
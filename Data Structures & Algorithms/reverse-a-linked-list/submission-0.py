# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr is not None:
            nxt = curr.next  # Save the next node
            curr.next = prev  # Flip pointer backwards
            prev = curr # Move previous forwards
            curr = nxt # Move next
        
        return prev 


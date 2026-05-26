# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        tail = dummy  # Create an empty linkedlist


        while list1 and list2:  # Iterate through both lists
            if list1.val < list2.val:  # if one value is bigger than other
                tail.next = list1  # Set next node to be smaller value
                list1 = list1.next  # Move forward in iteration
            else:             # list2 has the bigger or equal value
                tail.next = list2 # Set next node to be smaller value
                list2 = list2.next # Move forward in iteration
            
            tail = tail.next
        
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        
        return dummy.next

        
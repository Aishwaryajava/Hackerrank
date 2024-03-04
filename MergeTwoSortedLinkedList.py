# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # If one of the lists is empty, return the other list
        if not list1:
            return list2
        elif not list2:
            return list1
        
        # Initialize a dummy head node
        head = ListNode(0)
        # Initialize pointer to the dummy head
        current = head
        
        # Traversing through lists and checking if list1 is smaller than list2.
        while list1 is not None and list2 is not None:
            # If list1 value is smaller than list2 value, append list1 to the merged list
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            # Else, append list2 to the merged list
            else:
                current.next = list2
                list2 = list2.next
        
        # Move to the next node in the merged list
            current = current.next
        
        # Allocating the empty list of either of the nodes, append them to the merged list
        if list1 is not None:
            current.next = list1
        elif list2 is not None:
            current.next = list2

        # Return the merged list
        return head.next

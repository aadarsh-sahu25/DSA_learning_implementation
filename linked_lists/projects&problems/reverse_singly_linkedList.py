'''
    Given the head of a singly linked list, reverse the list, and return the reversed list.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        prev=None
        while temp:
            temp2=temp.next
            temp.next=prev
            prev=temp
            temp=temp2
            if temp is None:
                head=prev
                return head
# using pointers temp and temp2 to hold the current and next node making the last element as head

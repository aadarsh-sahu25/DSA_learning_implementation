'''
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

''' approach 1: first get the size of the list(probably not always a good approach as req. extra traversal for size) '''
'''
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t=head
        c=0
        while t:
            c+=1
            t=t.next
        if c==0:
            return head
        
        t=head
        i=1
        while i!=c//2+1:
            t=t.next
            i+=1
        return t
    '''
# two pointer appraoch
 class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow

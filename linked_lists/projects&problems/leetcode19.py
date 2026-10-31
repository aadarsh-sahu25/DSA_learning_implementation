'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.
  
Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''approach 1'''
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        count=0
        while temp:
            temp=temp.next
            count+=1
            
        i=1
        temp=head
        while i<count-n:
            temp=temp.next
            i+=1
        if temp.next is None or count==n:
            head=head.next
        else:
            temp.next=temp.next.next
        return head
            

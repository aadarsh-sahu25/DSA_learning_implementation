'''
SORTING OF LINKED LIST:
we prefer merge sort algprithm for sorting linked list because it's time complexity is O(nlogn) ( we use slow and fast pointer to get the mid node and then split list into two equal halves
recursively until we get single nodes elements and then position the value of those elements into a new list(say dummy) by comparising ).

quick sort have also time complexity O(nlogn) and is a in-place sorting algorithm but ,this algorithm req. direct access of element(choosing the pivot and placing at its posn) 
while linked list does not allow direct access of its elements(unlike array). That's why we prefer Merge sort algorithm.
'''



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        nextHalf=slow.next
        slow.next=None
        l=self.sortList(head)
        r=self.sortList(nextHalf)

        dummy=ListNode()
        temp=dummy
        while l and r:
            if l.val<=r.val:
                temp.next=l
                l=l.next
            else:
                temp.next=r
                r=r.next
            temp=temp.next
        
        if l:
            temp.next=l
        else:
            temp.next=r
        return dummy.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        curr = head
        dummy =init1 = ListNode(0)
        dummy2 =init2 = ListNode(0)
        while curr:
            if curr.val < x:
                dummy.next = curr
                dummy = dummy.next
            else:
                dummy2.next = curr
                dummy2 = dummy2.next
            curr = curr.next 
        dummy.next = init2.next
        dummy2.next = None
        return init1.next

        

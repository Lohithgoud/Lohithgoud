# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        temp = dummy
        pq = []

        for i in range(len(lists)):
            if lists[i] is not None:
                heapq.heappush(pq,(lists[i].val,i,lists[i]))

        while pq:
            nums, i , node = heapq.heappop(pq)
            temp.next = node
            temp = temp.next

            if node.next is not None:
                heapq.heappush(pq,(node.next.val,i , node.next))

        return dummy.next






        

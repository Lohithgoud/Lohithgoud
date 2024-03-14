def middlenode(self,head):
    fast = head
    while fast and fast.next:
        head= head.next
        fast = fast.next.next
    return head
# return address of middle number
# if we want value of middle number then "head.val"
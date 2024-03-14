def ispalindrome(self,head):
    if head is None:
        return True
    #split into teo parts
    slow = head
    fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

# reversing second part
    prev = None
    curr = slow
    while curr:
        curr = head 
        temp = head.next
        curr.next = prev
        prev = curr
        curr = temp

#check node by node for palindroine:
    first = head
    second = prev
    while second:
        if first.val != second.val:
            return False
        first = first.next
        second = second.next
    return True

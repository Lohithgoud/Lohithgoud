# reverse linked list 

def reverselist(self,head):
    prev = None
    while head:
        cur = head 
        head = head.next
        cur.next = prev
        prev = cur
    return prev

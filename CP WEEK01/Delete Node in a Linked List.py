#Delete Node in a Linked List (237) in leet code
def delNode(self,dnode):
    dnode.val = dnode.next.val
    dnode.next = dnode.next.next



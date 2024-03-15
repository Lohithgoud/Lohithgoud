# integer to Linkedlist
# input 128
# ouoput Linked List
# 1-> 2-> 8->


class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
        
    def createLL(self,l):
        for x in l:
            new=Node(x)
            if self.head==None:
                self.head=new
            else:
                t=self.head
                while t.next!=None:
                    t=t.next
                t.next=new
    def display(self,head):
        t=head
        print("Linked List")
        while t:
            print(t.val,end="-> ")
            t=t.next
    
n=int(input())
s=str(n)
o=Linkedlist()
o.createLL(s)
o.display(o.head)

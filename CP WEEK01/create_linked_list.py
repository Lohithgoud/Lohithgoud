class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def createLL(self,n):
        i=0
        while i<n:
            data=int(input("enter data : "))
            new_node=Node(data)
            if self.head==None:
                self.head=new_node
            else:
                curr_node=self.head
                while curr_node.next!=None:
                    curr_node=curr_node.next
                curr_node.next=new_node
            i=i+1
    def show(self,head):
        t=head
        while t:
            print(t.data,end=' ')
            t=t.next
        print("\n")
        
    
obj=LinkedList()
n=int(input("enter number of nodes to be inserted : "))
obj.createLL(n)
obj.show(obj.head)

        

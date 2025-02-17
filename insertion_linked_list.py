class node:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = node(10) 
node2 = node(20)
node3 = node(30)
node4 = node(40)

node1.next = node2
node2.next = node3
node3.next = node4

#insertion at begin
newnode = node(50)
head = node1
newnode.next = head
head = newnode

#insertion at between
newnode2 = node(25)
head = node1
current = head
while current is not None and current.data != 20:
    current = current.next
newnode2.next = current.next
current.next = newnode2


#insertion at end
newnode1 = node(60)
current = head
while current.next is not None:
    current = current.next
current.next = newnode1
 

current1 = head
while current1 is not None:
    print(current1.data, end=("->"))
    current1 = current1.next


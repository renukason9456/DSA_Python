class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next   
        current.next = prev        
        prev = current
        current = next_node

    return prev  # New head of the reversed list


def print_list(head):
    current = head
    while current:
        print(current.data, end=" -> " if current.next else "")
        current = current.next
    print()  # New line after printing list


# Creating linked list
node1 = Node(10) 
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4
head = node1

# Printing original list
print("Original Linked List:")
print_list(head)

# Reversing and printing the reversed list
head = reverse_list(head)
print("Reversed Linked List:")
print_list(head)



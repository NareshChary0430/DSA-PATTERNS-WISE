class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 

# Printing the linked list
def print_list(head):
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next


# Insert at the beginning of the linked list
def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    head = new_node
    return head

# Insert at the end of the linked list
def insert_at_end(head, data):
    new_node = Node(data)
    if head is None:
        head = new_node
        return head

    temp = head
    while temp.next:
        temp = temp.next
    temp.next = new_node
    return head

def insert_at_position(head, data, position):
    new_node = Node(data)
    if position == 0:
        new_node.next = head
        head = new_node
        return head

    temp = head
    for i in range(position - 1):
        if temp is None:
            print("Position out of bounds")
            return head
        temp = temp.next

    new_node.next = temp.next
    temp.next = new_node
    return head


# delete at the beginning of the linked list
def delete_at_beginning(head):
    if head is None:
        print("List is empty")
        return head
    head = head.next
    return head


# delete at the end of the linked list
def delete_at_end(head):
    if head is None:
        print("List is empty")
        return head
    if head.next is None:
        head = None
        return head

    temp = head
    while temp.next.next:
        temp = temp.next
    temp.next = None
    return head

# delete at value in the linked list
def delete_by_value(head, value):
    if head is None:
        print("List is empty")
        return head
    if head.data == value:
        head = head.next
        return head

    temp = head
    while temp.next:
        if temp.next.data == value:
            temp.next = temp.next.next
            return head
        temp = temp.next

    print("Value not found in the list")
    return head


head = Node(10)
second = Node(20)
third = Node(30)

head.next = second
second.next = third

# Printing the linked list
# print_list(head)

# Inserting a new node at the beginning of the linked list
head = insert_at_beginning(head, 5)
# print_list(head)

# Inserting a new node at the end of the linked list
head = insert_at_end(head, 40)
# print_list(head)

# Inserting a new node at position 2 of the linked list
head = insert_at_position(head, 25, 2)
# print_list(head)

# Deleting a node at the beginning of the linked list
head = delete_at_beginning(head)
# print_list(head)

# Deleting a node at the end of the linked list
head = delete_at_end(head)
# print_list(head)
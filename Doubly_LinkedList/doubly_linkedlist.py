class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_linkedlist(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        
        if self.head is None:
            return None
        
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        #return temp.value
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True



    def pop_first(self):
        pass

    def insert(self):
        pass

    def remove(self):
        pass

    def reverse(self):
        pass

# Create and append first doubly linkedlist element
my_doubly_linkedlist = DoublyLinkedList(2)
my_doubly_linkedlist.append(3)
my_doubly_linkedlist.print_linkedlist()
my_doubly_linkedlist.prepend(1)
my_doubly_linkedlist.print_linkedlist()
# # (2) Items - Return 2nd Node
# print(my_doubly_linkedlist.pop())
# # (1) Items - Return 1st Node
# print(my_doubly_linkedlist.pop())
# # (0) Items - Return None
# print(my_doubly_linkedlist.pop())
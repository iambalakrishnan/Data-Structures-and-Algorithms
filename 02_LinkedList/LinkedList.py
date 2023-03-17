class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
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
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
    
    #Check the node is already none
        if self.length == 0:
            return None

        pre = self.head
        temp = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1

        # After deleting node with one element
        if self.length == 0:
            self.head = None
            self.tail = None
        

        return [temp, temp.value]
    



# #creating node and append operation 
# my_linked_list = LinkedList(1)
# my_linked_list.append(2)
# my_linked_list.append(3)
# my_linked_list.print_linkedlist()


# Pop operation for multiple element
my_linked_list = LinkedList(1)
my_linked_list.append(2)
# (2) Items - Return 2 Node
print(my_linked_list.pop())
# (1) Items - Return 1 Node
print(my_linked_list.pop())
# (0) Items - Return 0 Node
print(my_linked_list.pop())
my_linked_list.print_linkedlist()

# # Pop operation for single element
# my_linked_list = LinkedList(1)
# my_linked_list.print_linkedlist()
# # (0) Items - Return 0 Node
# print(my_linked_list.pop())





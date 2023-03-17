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
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None

        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        # after poping out element which has only one element in it
        if self.length == 0:
            self.tail = None
        return temp
            
    def get(self, index):
        if index < 0 or index > self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_values(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
        
    def remove(self, index):
        print(f"index value is {index}")
        if index < 0 or index > self.length:
            return None # here we are returning a node
        if index == 0:
            print(self.length)
            return self.pop_first()
        if index == self.length:
            print(f"length is {self.length}")
            return self.pop()
        
        print(f"length is {self.length}")
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return [temp, temp.value]
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after




# #creating node and append operation 
# my_linked_list = LinkedList(1)
# my_linked_list.append(2)
# my_linked_list.append(3)
# my_linked_list.print_linkedlist()


# # Pop operation for multiple element
# my_linked_list = LinkedList(1)
# my_linked_list.append(2)
# # (2) Items - Return 2 Node
# print(my_linked_list.pop())
# # (1) Items - Return 1 Node
# print(my_linked_list.pop())
# # (0) Items - Return 0 Node
# print(my_linked_list.pop())
# my_linked_list.print_linkedlist()


# my_linked_list = LinkedList(2)
# my_linked_list.append(3)
# print("before prepend : \n")
# my_linked_list.print_linkedlist()
# print(my_linked_list.prepend(1))
# print("after prepend : \n")
# my_linked_list.print_linkedlist()


# # Pop_first with multiple element
# my_linked_list = LinkedList(1)
# my_linked_list.append(2)
# my_linked_list.print_linkedlist()
# # (2) Items - Return 2 Node
# print(my_linked_list.pop_first())
# # (1) Items - Return 1 Node
# print(my_linked_list.pop_first())
# # (0) Items - Return 0 Node
# print(my_linked_list.pop_first())


# # Pop_first with multiple element
# my_linked_list = LinkedList(1)
# my_linked_list.append(2)
# my_linked_list.print_linkedlist()
# # (2) Items - Return 2 Node
# print(my_linked_list.pop_first())
# # (1) Items - Return 1 Node
# print(my_linked_list.pop_first())
# # (0) Items - Return 0 Node
# print(my_linked_list.pop_first())

# # Get Index 
# my_linked_list = LinkedList(10)
# my_linked_list.append(20)
# my_linked_list.append(30)
# my_linked_list.append(40)
# print(my_linked_list.get(3))
# print(my_linked_list.get(0))
# print(my_linked_list.get(2))
# print(my_linked_list.get(5))
# print(my_linked_list.get(-1))

# #set_values for particular index 
# my_linked_list = LinkedList(10)
# my_linked_list.append(20)
# my_linked_list.append(30)
# my_linked_list.append(40)
# my_linked_list.set_values(3,45)
# my_linked_list.print_linkedlist()
# print(my_linked_list.set_values(0, 15))
# my_linked_list.print_linkedlist()
# print(my_linked_list.set_values(5, 55))


# #insert at a particular index 
# my_linked_list = LinkedList(0)
# my_linked_list.print_linkedlist()
# # my_linked_list.insert(0,0)
# my_linked_list.insert(1,1)
# my_linked_list.print_linkedlist()

# #remove at a particular index 
# my_linked_list = LinkedList(0)
# my_linked_list.append(1)
# my_linked_list.append(2)
# my_linked_list.append(3)
# my_linked_list.print_linkedlist()
# print(my_linked_list.remove(3))
# # print(my_linked_list.remove(0))
# # print(my_linked_list.remove(0))
# my_linked_list.print_linkedlist()

#reverse a linkedlist
my_linked_list = LinkedList(0)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.print_linkedlist()
my_linked_list.reverse()
my_linked_list.print_linkedlist()

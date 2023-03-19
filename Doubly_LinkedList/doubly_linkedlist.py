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
        
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        #return [temp, temp.value]
        return temp

    def get(self, index):
        if index < 0 or index > self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        # return [temp, temp.value]
        return temp
    
    def set_value(self, index, value):
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
        before = self.get(index - 1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        
        self.length += 1 
        return True

    def remove(self, index):
        if index < 0 or index > self.length:
            return None # here we are returning a node
        if index == 0:
            print(self.length)
            return self.pop_first()
        if index == self.length - 1:
            print(f"length is {self.length}")
            return self.pop()
        temp = self.get(index)
        
        temp.next.prev =  temp.prev
        temp.prev.next = temp.next
        temp.prev = None
        temp.next = None
        
        self.length -= 1
        # return [temp, temp.value]
        return temp
        

    def reverse(self):
        first = None
        second = self.head
        
        while second is not None:
            first = second.prev
            second.prev = second.next
            second.next = first
            second = second.prev

        if first is not None:
            self.head = first.prev  

# # Create and append first doubly linkedlist element
# my_doubly_linkedlist = DoublyLinkedList(0)
# my_doubly_linkedlist.append(1)
# my_doubly_linkedlist.append(2)
# my_doubly_linkedlist.print_linkedlist()
# #prepend 
# my_doubly_linkedlist.prepend(1)
# # (2) Items - Return 2nd Node
# print(my_doubly_linkedlist.pop())
# # (1) Items - Return 1st Node
# print(my_doubly_linkedlist.pop())
# # (0) Items - Return None
# print(my_doubly_linkedlist.pop())

# # pop first
# print(my_doubly_linkedlist.pop_first())
# print(my_doubly_linkedlist.pop_first())
# print(my_doubly_linkedlist.pop_first())

# # get()
# print(my_doubly_linkedlist.get(0))
# print(my_doubly_linkedlist.get(2))

# # set_value()
# print(my_doubly_linkedlist.set_value(0,10))
# my_doubly_linkedlist.print_linkedlist()
# print(my_doubly_linkedlist.set_value(2,20))
# my_doubly_linkedlist.print_linkedlist()

# # insert()
# my_doubly_linkedlist.insert(1,10)
# my_doubly_linkedlist.print_linkedlist()

# # remove()
# print(my_doubly_linkedlist.remove(1), "\n")
# my_doubly_linkedlist.print_linkedlist()

# Reverse a linkedlist
my_doubly_linkedlist = DoublyLinkedList(0)
my_doubly_linkedlist.append(1)
my_doubly_linkedlist.append(2)
my_doubly_linkedlist.print_linkedlist()
my_doubly_linkedlist.reverse()
my_doubly_linkedlist.print_linkedlist()

class Node:
    def __init__(self, value):
        self.value =  value
        self.next = None

        # {
        #     "value": 4,
        #     "next": None
        # }
class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True
    
    def dequeue(self):
        if self.first is None:
            return None
        temp = self.first
        if self.first.next is None:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        # return [temp, temp.value]
        return temp




my_queue = Queue(1)
my_queue.enqueue(2)
my_queue.print_queue()
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
my_queue.print_queue()
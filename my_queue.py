class Queue:
    class Node:
        def __init__(self,data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        self.last = None
        self.size = 0


    def is_empty(self): #time complexity : tete(1)
        return self.size == 0

    def enqueue(self,data): #time complexity : tete(1)
        new = self.Node(data)
        if self.is_empty():
            self.head = new
        else:
            self.tail.next = new
        self.tail = new
        self.size += 1

    def dequeue(self): #time complexity : tete(1)
        if self.is_empty():
            raise AssertionError('empty queue can not dequeue')
        result = self.head.data
        self.head = self.head.next
        self.size -= 1
        if self.is_empty():
            self.last = None
        return result

    def Size(self):
        return self.size

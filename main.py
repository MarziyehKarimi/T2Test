from my_queue import Queue
from my_stack import Stack

class Characters:
    def __init__(self):
        self.queue = Queue()
        self.stack = Stack()

    def push(self,element):
        if (self.stack.Top()+self.queue.Size())%2 == 0:
            return self.stack.push(element)
        self.queue.enqueue(element)

    def pop(self):
        if not(self.stack.is_empty()):
            return self.stack.pop()
        return self.queue.dequeue()

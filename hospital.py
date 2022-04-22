from my_queue import Queue

class Hospital:
    def __init__(self):
        self.normal = Queue()
        self.serious = Queue()
        self._exit = 0

    def push(self,element,priority):
        if priority == 1:
            return self.serious.enqueue(element)
        self.normal.enqueue(element)

    def pop(self):
        if (not(self.serious.is_empty()) and self.serious_exit(3)) or self.normal.is_empty():
            self._exit += 1
            return self.serious.dequeue()
        return self.normal.dequeue()

    def serious_exit(self,n):
        if self._exit == 0:
            return True
        return self._exit % n != 0

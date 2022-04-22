class Stack:
    def __init__(self,size=50):
        self.size = size
        self.S = [None]*size
        self.top = 0

    def push(self,element):
        assert self.top < self.size ,'stack is full'         
        self.S[self.top] = element
        self.top += 1
                
    def pop(self):
        assert self.top != 0 ,'stack is empty' 
        pop_element = self.S[self.top-1]
        self.S[self.top-1]= None
        self.top -= 1
        return pop_element

    def is_empty(self):
        if self.top <= 0:
            return True
        return False

    def Top(self):
        return self.top

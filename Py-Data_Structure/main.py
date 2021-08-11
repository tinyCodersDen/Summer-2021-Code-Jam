class Stack:
    def __init__(self): self.stack = []
    def push(self,element):
        if type(element) != list:
            self.stack.append(element)
        else:
            for t in element:
                self.stack.append(t)
    def pop(self): self.stack.pop(-1)
    def top(self): return self.stack[-1]
    def bottom(self): return self.stack[0]
    def isEmpty(self):
        if len(self.stack)>=1:
            return False
        else:
            return True
    def get_stack(self): return self.stack
    def size(self): return len(self.stack)
class Queue:
    def __init__(self): self.queue = []
    def enqueue(self,element):
        if type(element) != list:
            self.queue.append(element)
        else:
            for t in element:
                self.queue.append(t)
    def dequeue(self): self.queue.pop(0)
    def front(self): return self.queue[0]
    def back(self): return self.queue[-1]
    def isEmpty(self):
        if len(self.queue)==0:
            return True
        else:
            return False
    def size(self): return len(self.queue)
    def get_queue(self): return self.queue

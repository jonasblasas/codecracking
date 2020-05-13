class Stack:
    def __init__(self):
        self.data = []

    def pop(self):
        if self.is_empty():
            return None
        val = self.data[len(self.data)-1]
        self.data = self.data[:len(self.data)-1]
        return val

    def peek(self):
        if self.is_empty():
            return None
        return self.data[len(self.data)-1]

    def push(self, val):
        self.data.append(val)

    def is_empty(self):
        return len(self.data) == 0


class Queue:
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def enqueue(self, val):
        self.in_stack.push(val)

    def dequeue(self):
        if self.out_stack.is_empty():
            if self.in_stack.is_empty():
                return None
            while self.in_stack.is_empty() == False:
                self.out_stack.push(self.in_stack.pop())
        return self.out_stack.pop()

    def peek(self):
        if self.out_stack.is_empty():
            if self.in_stack.is_empty():
                return None
            while self.in_stack.is_empty() == False:
                self.out_stack.push(self.in_stack.pop())
        return self.out_stack.peek()

    def is_empty(self):
        return self.in_stack.is_empty() and self.out_stack.is_empty

def print_queue(q):
    s = "["
    for i in range(0, len(q.out_stack.data)):
        s += str(q.out_stack.data[i])
        if i < len(q.out_stack.data)-1:
            s += ", "
    for i in range(0, len(q.in_stack.data)):
        s += str(q.in_stack.data[i])
        if i < len(q.in_stack.data)-1:
            s += ", "
    s += "]"
    print(s)

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

# should print [1, 2, 3]
print_queue(queue)

v = queue.dequeue()

# should print [2, 3]
print_queue(queue)

v = queue.dequeue()

# should print [3]
print_queue(queue)

queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)

v = queue.dequeue()

# should print [4, 5, 6]
print_queue(queue)

v = queue.dequeue()
v = queue.dequeue()
v = queue.dequeue()
print_queue(queue)
v = queue.dequeue()
print_queue(queue)
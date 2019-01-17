class Stack:

    def __init__(self, size):
        self.stack = [size]
        self.max_size = size

    # Adding elements
    def push(self, s):
        if self.size() < self.max_size:
            self.stack.append(s)
        else:
            self.stack.pop(0)
            self.push(s)

    # Deleting elements
    def pop(self):
        if not self.empty():
            self.stack.pop(len(self.stack)-1)

    # Returns size of stack
    def size(self):
        return len(self.stack)

    # Returns last element
    def top(self):
        if not self.empty():
            return self.stack[len(self.stack)-1]

    # Checks if stack is empty
    def empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

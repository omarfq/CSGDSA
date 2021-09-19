class MyStack():
    def __init__(self):
        self.array = []
        self.size = 0

    def push(self, data):
        self.array.append(data)
        self.size += 1

    def pop(self):
        self.size -= 1
        return self.array.pop()

    def is_empty(self):
        return self.size == 0
    
    def length(self):
        return self.size

def reverse_string(s):
    stack = MyStack()
    new_str = ''
    for letter in s:
        stack.push(letter)
    while stack.length() > 0:
        new_str += stack.pop()
    return new_str

print(reverse_string('abcde'))
    

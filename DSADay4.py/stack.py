# import sys

# class Stacks:
#     def __init__(self):
#         self.stack=[]
#         self.top=-1
#         self.CAPACITY=5
#     def isFull(self):
#         if self.top == self.CAPACITY-1:
#             return True
#         else:
#             return False
#     def push(self,ele):
#         if self.isFull():
#             print("Stack is Full")
#         else:
#             self.top=self.top+1
#             self.stack.append(ele)
#             print(ele, "is pushed")
#     def traverse(self):
#         for i in range(self.top,-1,-1):
#             print(self.stack[i])    
#     def pop(self):
#         pass
#     def peek(self):
#         pass
    
# if __name__ == '__main__':
#     obj=Stacks()
#     while True:
#         print("1. Push")
#         print("2. Pop")
#         print("3. Peek")
#         print("4. Traverse")
#         print("0. Exit")
#         ch=int(input("Select any Choice: "))
#         if ch == 1:
#             ele=int(input("Enter Data: "))
#             obj.push(ele)
#         elif ch == 2:
#             obj.pop()
#         elif ch == 3:
#             obj.peek()
#         elif ch == 4:
#             obj.traverse()
#         elif ch == 0:
#             sys.exit(0)



#reverse array using stack

import sys

class Stacks:
    def __init__(self):
        self.stack = []
        self.top = -1
        self.CAPACITY = 100

    def isFull(self):
        return self.top == self.CAPACITY - 1

    def isEmpty(self):
        return self.top == -1

    def push(self, ele):
        if self.isFull():
            print("Stack is Full")
        else:
            self.top += 1
            self.stack.append(ele)

    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
            return None
        else:
            ele = self.stack.pop()
            self.top -= 1
            return ele

    def peek(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            print("Top Element:", self.stack[self.top])

    def traverse(self):
        for i in range(self.top, -1, -1):
            print(self.stack[i])


# Reverse Array Using Stack
arr = [234235,235,235,235,5]

obj = Stacks()

# Push array elements into stack
for i in arr:
    obj.push(i)

# Pop elements back into array
for i in range(len(arr)):
    arr[i] = obj.pop()

print("Reversed Array:", arr)

#reverse the string using stack
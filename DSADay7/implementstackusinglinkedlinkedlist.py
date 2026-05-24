#implement a stack using singly linked list

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# class Stack:
#     def __init__(self):
#         self.top = None

#     def push(self, data):
#         new_node = Node(data)
#         new_node.next = self.top
#         self.top = new_node
#     def pop(self):
#         if self.top is None:
#             print("Stack is empty")
#         else:
#             print("Deleted:", self.top.data)
#             self.top = self.top.next

#     def display(self):
#         temp = self.top

#         if self.top is None:
#             print("Stack is empty")
#         else:
#             while temp:
#                 print(temp.data)
#                 temp = temp.next


# obj = Stack()

# while True:
#     print("\n1. Push")
#     print("2. Pop")
#     print("3. Display")
#     print("4. Exit")

#     ch = int(input("Enter choice: "))

#     if ch == 1:
#         data = int(input("Enter data: "))
#         obj.push(data)

#     elif ch == 2:
#         obj.pop()

#     elif ch == 3:
#         obj.display()

#     elif ch == 4:
#         break

#     else:
#         print("Invalid choice")



#example
# stock span problem
# example 1:
# Input:
# N = 7, Price[] = [100 80 60 70 60 75 85]
# output:
# 1 1 1 8 1 8 8
# Explanation:
#    traversing the given input span for 100 will be 1,
#     80 is smaller than 100 so the span is 1,
# 60 is smaller than 80 so the span is 1,
# 70 is greater  than 60 so the span is 2,
# 60 is smaller than 70 so the span is 1,
# 75 is greater than 75 so the span is 2,
# 85 is greater than 75 so the span is 2,
# hence the output will be 1 1 1 2 1 2 2



# Stock Span Problem Using Stack

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0


def stockSpan(price):
    n = len(price)

    span = [0] * n

    st = Stack()

    # First element span is always 1
    st.push(0)
    span[0] = 1

    for i in range(1, n):

        # Pop elements smaller than current price
        while (not st.isEmpty()) and (price[st.peek()] <= price[i]):
            st.pop()

        # If stack becomes empty
        if st.isEmpty():
            span[i] = i + 1
        else:
            span[i] = i - st.peek()

        # Push current index
        st.push(i)

    return span


# Driver Code
price = [100, 80, 60, 70, 60, 75, 85]

result = stockSpan(price)

print("Stock Span:", result)
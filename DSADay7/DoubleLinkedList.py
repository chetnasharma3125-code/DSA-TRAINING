# import sys
# class GetNode:
#     def __init__(self):
#         self.left=None
#         self.data=None
#         self.right=None

# class LinkedList:
#     def __init__(self):
#         self.head=None

#     def append(self):
#         data=int(input("Enter data: "))
#         newNode=GetNode()
#         newNode.data=data
#         if self.head is None:
#             self.head=newNode
#         else:
#             ptr=self.head
#             while ptr.right!=None:
#                 ptr=ptr.right
#             ptr.right=newNode
#             newNode.left=ptr
#             print(data, "is added") 


#     def traverse(self):
#         if self.head is None:
#             print("List not present")
#         else:
#             ptr=self.head
#             while ptr!=None:
#                 print(ptr.data," -> ",end="")
#                 ptr=ptr.right


#     def AddatBeg(self):
#         newnode = node(data)
#         if self.head is None:
#             self.head = newnode
#         else:
#             newnode.next=self.head
#             self.head.prev = newnode
#             self.head=newnode




# if __name__ =='__main__' :
#      obj=LinkedList()
#      while True:
#          print("\n1. Append ")  
#          print("2. Traverse ") 
#          print("3. Add at Begin")
#          print("0. Exit")
#          n=int(input("Select any choice: "))
#          if n==1:
#              obj.append()
#          elif n==2:
#              obj.traverse()
#          elif n==3:
#              obj.AddatBeg()
#          elif n==0:
#              sys.exit(0)




import sys

class GetNode:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Append at end
    def append(self):

        data = int(input("Enter data: "))

        newNode = GetNode()
        newNode.data = data

        if self.head is None:
            self.head = newNode

        else:
            ptr = self.head

            while ptr.right is not None:
                ptr = ptr.right

            ptr.right = newNode
            newNode.left = ptr

        print(data, "is added")

    # Traverse
    def traverse(self):

        if self.head is None:
            print("List not present")

        else:
            ptr = self.head

            while ptr is not None:
                print(ptr.data, end=" <-> ")
                ptr = ptr.right

            print("None")

    # Add at beginning
    def AddatBeg(self):

        data = int(input("Enter data: "))

        newNode = GetNode()
        newNode.data = data

        if self.head is None:
            self.head = newNode

        else:
            newNode.right = self.head
            self.head.left = newNode
            self.head = newNode

        print(data, "added at beginning")

    # Add in between after a value
    def AddinBetween(self):

        value = int(input("Enter node value after which to insert: "))
        data = int(input("Enter new data: "))

        ptr = self.head

        while ptr is not None and ptr.data != value:
            ptr = ptr.right

        if ptr is None:
            print("Node not found")

        else:
            newNode = GetNode()
            newNode.data = data

            newNode.right = ptr.right
            newNode.left = ptr

            if ptr.right is not None:
                ptr.right.left = newNode

            ptr.right = newNode

            print(data, "inserted")

    # Delete at end
    def DeleteAtEnd(self):

        if self.head is None:
            print("List is empty")

        elif self.head.right is None:
            print(self.head.data, "deleted")
            self.head = None

        else:
            ptr = self.head

            while ptr.right is not None:
                ptr = ptr.right

            print(ptr.data, "deleted")

            ptr.left.right = None


if __name__ == '__main__':

    obj = LinkedList()

    while True:

        print("\n1. Append")
        print("2. Traverse")
        print("3. Add at Beginning")
        print("4. Add in Between")
        print("5. Delete at End")
        print("0. Exit")

        n = int(input("Select any choice: "))

        if n == 1:
            obj.append()

        elif n == 2:
            obj.traverse()

        elif n == 3:
            obj.AddatBeg()

        elif n == 4:
            obj.AddinBetween()

        elif n == 5:
            obj.DeleteAtEnd()

        elif n == 0:
            sys.exit(0)

        else:
            print("Invalid choice")
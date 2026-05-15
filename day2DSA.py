# arr=[[1,2,3],22,[4,5]]
# print(arr)
# for x in range(len(arr)):
#     print(arr[x])

# arr=[[1,2,3],[4,5,6],[7,8,9]]
# print(arr)
# for x in range(len(arr)):
#     print(arr[x])

# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         print(arr[i][j],end=" ")
#         print()


# t=()
# t=tuple()
# t=(23,24,234,432,34)
# print(t)
# print(type(t))


#set
# s=set()
# print(s)
# print(type(s))

# s={1,2,4,5,3,6,7,3,4,5}
# print(s)

# arr=[1,2,3,4,5,3,2,4,3,2,4,4]
# s=set(arr)
# arr=list(s)
# print(arr)


#accept values from user and print it
# n=int(input("Enter size: "))
# print("Enter list elements: ")
# arr=[]
# for i in range(n):
#     element=int(input("Enter element: "))
#     arr.append(element)

# for i in range(len(arr)):
#     print(arr[i])


# a=int(input())

# a=int(input())
# b=int(input())

# a,b=map(int,input().split())

#accept values from user find sum of list
# n = int(input("Enter number of elements: "))
# numbers = []

# for i in range(n):
#     value = int(input("Enter element: "))
#     numbers.append(value)
# total_sum = sum(numbers)
# print("The sum of the list is:", total_sum)

#sum of even and odd numbers in a list
# n = int(input("Enter size: "))
# print("Enter list elements: ")
# arr = []
# even = 0
# odd = 0
# for i in range(n):
#     element = int(input("Enter element: "))
#     arr.append(element)
# for num in arr:
#     if num % 2 == 0:
#         even += num
#     else:
#         odd += num
# print("Sum of even numbers:", even)
# print("Sum of odd numbers:", odd)


#sum of even and odd numbers in a list
n = int(input("Enter size: "))
print("Enter list elements: ")  
arr = []
even = 0
odd = 0
for i in range(n):
    element = int(input("Enter element: "))
    arr.append(element)
for num in arr:
    if num % 2 == 0:
        even += num
    else:
        odd += num
print("Sum of even numbers:", even)
print("Sum of odd numbers:", odd)
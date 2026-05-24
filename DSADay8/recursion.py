# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)
    


# if __name__ == '__main__':
#     n=5
#     res=fact(n)
#     print(res)




# def multiply(x,y):
#     if y==1:
#         return x
#     elif x==1:
#         return y
#     elif x==0 or y==0:
#         return 0
#     else:
#         return x+multiply(x,y-1)
    

#find power using recursion
#Find Power using Recursion
def power(x,y):
  if y==0:
    return 1
  else:
    return x*power(x,y-1)
if __name__ == '__main__':
  x=3
  y=2
  res=power(x,y)
  print(res)

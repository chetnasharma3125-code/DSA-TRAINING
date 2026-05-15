# for i in range(1,5):
#     for j in range(1,5):
#         print(i,end=" ")
#     print()


# for i in range(1,5):
#     for j in range(1,5):
#         print(j,end=" ")
#     print()


# n=1
# for i in range(1,5):
#     for j in range(1,5):
#         print(n,end="\t")
#         n=n+1
#     print()


#print char
# n=65
# for i in range(1,5):
#     for j in range(1,5):
#         print(chr(n),end="\t")
#         n=n+1
#     print()


# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end="\t")
#     print()


# for i in range(4,0,-1):
#     for j in range(1,i+1):
#         print("*",end="\t")
#     print()


sp=0
for i in range(4,0,-1):
    for x in range(sp):
        print(end="\t")
    for j in range(1,i+1):
        print("*",end="\t")
    print()
    sp=sp+1
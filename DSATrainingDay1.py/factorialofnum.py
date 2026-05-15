#factorial of a number
no=int(input("Enter a number: "))
fact=1
while no>0:
    fact=fact*no
    no=no-1
    print(fact)
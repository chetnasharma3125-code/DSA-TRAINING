#count the digits
no=int(input("Enter a number: "))
count=0     
while no>0:
    no=no//10
    count=count+1
print(count)
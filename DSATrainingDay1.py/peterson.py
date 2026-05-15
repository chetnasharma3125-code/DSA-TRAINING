#peterson number or not
no=int(input("Enter a number: "))
no=0
save=no
fact=1
sum=0
while no>0:
    rem=no%10
    for i in range(1,rem+1):
        fact=fact*i
    sum=sum+fact
    no=no//10
if sum==save:
    print("no is peterson")
else:
    print("no is not peterson")
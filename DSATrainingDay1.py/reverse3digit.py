#reverse of 3 digit number
no=int(input("Enter a number: "))
n1=no%10
no=no//10
n2=no%10   
no=no//10
n3=no%10
rev=(n1*100)+(n2*10)+(n3*1)
print(rev)
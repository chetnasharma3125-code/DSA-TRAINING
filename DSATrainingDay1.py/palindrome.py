#number is palindrome or not
no=int(input("Enter a number: "))
no=0
save=no
rev=0
while no>0:
    rem=no%10
    rev=(rev*10)+rem
    no=no//10
if save==rev:
    print("no is palindrome")
else:
    print("no is not palindrome")
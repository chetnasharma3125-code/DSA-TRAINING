#technumber
# no=int(input("Enter number: "))
# n1=no%100
# n2=no//100
# sum=n1+n2
# sq=sum*sum
# if sq==no:
#     print("Technumber")
# else:
#     print("Not a Technumber")

#six digit tech number
# no=int(input("Enter number: "))
# n1=no%1000
# n2=no//1000
# sum=n1+n2
# sq=sum*sum
# if sq == no:
#     print("Technumber")
# else:       
#     print("Not a Technumber")


#any number tech number
no=int(input("Enter number: "))
save=no
count=0

while no>0:
    no=no//10
    count=count+1
no=save
if count%2==0:
    mid=count//2
    n1=no%10**mid
    n2=no//10**mid
    sum=n1+n2
    sq=sum*sum
    if sq==no:
      print("Technumber")
    else:
        print("Not a Technumber")
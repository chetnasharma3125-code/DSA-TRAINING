#find
# # s="Learning Python is very easy"
# print(s.find("Python"))
# print(s.find("Java"))
# print(s.find("r"))
# print(s.rfind("r"))


#count
# s="abcabcabcabcadda"
# print(s.count("a"))
# print(s.count("ab"))
# print(s.count('a',3,10))

#replace
#s="Learning Python is very difficult from ashish Sir"
#s1=s.replace("difficult","easy")
#print(s1)

#split
# s="Learning Python is very easy"
# ls=s.split()
# print(ls)


# s="22-02-2022"
# ls=s.split("-")
# print(ls)

# s="www.ashish.com"
# ls=s.split(".")
# print(ls)


# #join
# ls=["Learning","Python","is","very","easy"]
# s=" ".join(ls)
# print(s)



#Q2. Program to reverse order of words
# s="Learning python is very easy from Ashish sir"
# ls=s.split()
# ls.reverse()
# s=" ".join(ls)
# print(s)

#Q3. program to reverse internal content of each word
# s="Learning python is very easy from Ashish sir"
# ls=s.split()
# for i in range(len(ls)):
#     ls[i]=ls[i][::-1]
# s=" ".join(ls)
# print(s)



#write a program to remove duplicate characters from the given input string
# s = "ABCDABBCDABBBCCCDDEEEF"
# result = ""
# for char in s:
#     if char not in result:
#         result += char
# print(result)


#Q accept mobile number check that mobile number is 10 digit and digit only. Check number is valid in india or not (6,7,8,9)
mobile = input("Enter mobile number: ")
if mobile.isdigit():
    if len(mobile) == 10:
        if mobile.startswith("6") or mobile.startswith("7") or mobile.startswith("8") or mobile.startswith("9"):
            print("Valid mobile number")
        else:
            print("Invalid mobile number")



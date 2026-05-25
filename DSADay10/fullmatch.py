import re
str=input("Enter any string : ")
m=re.fullmatch(str,"abcabcabc")
if m!=None:
    print("matching is available")
else:
    print("matching is not available")
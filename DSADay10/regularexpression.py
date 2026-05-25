import re
count=0
pattern=re.compile("ab")
matcher=pattern.finditer("abaababaab")
#print(matcher)
for match in matcher:
    count+=1
    print(match.start(),'...',match.end(),'...',match.group())
print("total no of group occurrences : ",count)



#pass pattern to finditer
import re
count=0
# pattern=re.compile("ab")
# matcher=pattern.finditer("abaababaab")
matcher=re.finditer("ab","abaababaab")
for match in matcher:
    count+=1
    print(match.start(), '...', match.end(), '...',match.group())
print("total no of group occurrences : ",count)


import re
x="[abc]"
x="[^abc]"
x="[a-z]"
x="[0-9]"
x="[a-zA-Z0-9]"
matcher=re.finditer(x,"a7bD2@k2$D8z")
# print(matcher)
for match in matcher:
    print(match.start(),'...',match.group()) 
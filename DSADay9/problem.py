n = int(input("Enter no of semester: "))

subjects = []
for i in range(1, n + 1):
    s = int(input(f"Enter no of subjects in {i} semester: "))
    subjects.append(s)

for i in range(1, n + 1):
    print(f"Marks obtained in semester {i}: ")
    marks = []
    valid = True
    for j in range(subjects[i - 1]):
        m = int(input())
        if m < 0 or m > 100:
            print("You have entered invalid mark.")
            valid = False
            break
        marks.append(m)
    
    if valid:
        print(f"Maximum mark in {i} semester:{max(marks)}")
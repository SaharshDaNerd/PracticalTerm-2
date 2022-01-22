#Create a dictionary that asks for roll number,marks and name of the student n number of times.
n = int(input("Enter the number of students: "))
d = {}
for i in range(n):
    roll = int(input("Enter the roll number: "))
    name = input("Enter the name: ")
    marks = int(input("Enter the marks: "))
    d[roll] = [name,marks]
#Print the name of students who scored more than 75 marks.
for i in d:
    if d[i][1]>75:
        print(d[i][0])

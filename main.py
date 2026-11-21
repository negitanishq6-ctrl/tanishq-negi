 
names = ["Rahul", "Aman", "Priya", "Riya", "Karan"]
marks = [70, 50, 90, 35, 80]

print("STUDENT MARKS DATA")

for i in range(5):
    print(names[i], ":", marks[i])

print("\nAverage Marks:", sum(marks) / len(marks))
print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))

print("\nStudents who passed:")
for i in range(5):
    if marks[i] >= 40:
        print(names[i])

print("\nStudents who failed:")
for i in range(5):
    if marks[i] < 40:
        print(names[i])

print("\nTotal Students:", len(names))

studentNumber = [i for i in range(1,31)]
for _ in range(28):
    student = int(input())
    studentNumber.remove(student)

print(min(studentNumber))
print(max(studentNumber))
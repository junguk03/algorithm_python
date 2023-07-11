studentNumber = list(map(int,input().split()))
num = []
num = [i for i in range(1,31)]
studentNumber = set(studentNumber)
num = set(num)
answer = list(num.difference(studentNumber))
answer.sort()
for i in range(0,2):
    print(answer[i])
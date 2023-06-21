n, m = map(int,input().split())
list = [0]*n
i = int(0)
for i in range(n):
    list[i] = i + 1
for i in range(m):
    a, b = map(int, input().split())
    box = list[a-1]
    list[a-1] = list[b-1]
    list[b-1] = box
for i in range(n):
    print(list[i])
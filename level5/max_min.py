a = int(input())
b = list(map(int,input().split()))
min = 1000001
max = -1000001
for i in range(a):
    if(b[i]<min):
        min = b[i]
    if(b[i]>max):
        max = b[i]

print(min, max)
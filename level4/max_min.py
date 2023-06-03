num = int(input())
num_list = list(map(int, input().split()))
max = -1000000
min = 1000000
for i in range(num):
    if(num_list[i]>max):
        max = num_list[i]
    elif(num_list[i]<min):
        min = num_list[i]
    else:
        continue
print(min,max)
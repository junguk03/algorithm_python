num = int(input())
num_list = list(map(int,input().split()))
special_num = int(input())
sum = 0
for i in range(0,num):
    if(num_list[i] == special_num):
        sum += 1
print(sum)

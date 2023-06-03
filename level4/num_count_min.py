num1, num2 = map(int, input().split())
num_list = list(map(int, input().split()))
num_list2 = []
sum = 0
for i in range(num1):
    if(num_list[i]<num2):
        num_list2.append(num_list[i])
        sum += 1
    else:
        continue
for i in range(sum):
    print(num_list2[i])
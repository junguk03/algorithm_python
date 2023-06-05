max = 0
sum = 0
for i in range(9):
    num = int(input())
    if(num>max):
        max = num
        sum = i + 1
print(max+"\n"+sum)

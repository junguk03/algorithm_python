size, number = map(int, input().split())
list = []
list = [0 for i in range(100)]
for i in range(number):
    start, last, num = map(int, input().split())
    for j in range(start-1,last):
        list[j] = num
for i in range(size):
    print(list[i])
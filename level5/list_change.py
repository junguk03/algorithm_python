a, b = map(int, input().split())
array = list()
for i in range(1,a+1):
    array.append(i)
for i in range(b):
    c, d = map(int,input().split())
    box = array[d-1]
    array[d-1] = array[c-1]
    array[c-1] = box
[print(array[i]) for i in range(a)]

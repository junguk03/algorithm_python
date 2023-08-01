x, y, w, h = list(map(int, input().split()))
num_list = [x,y,w-x,h-y]
min_num = min(num_list)
print(min_num)
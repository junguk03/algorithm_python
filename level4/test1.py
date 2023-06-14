print("주문내역: shirt_size = ['XS','S','M','L','XL','XXL']")
print("주문한 셔츠 사이즈별 개수: 'XS','S','M','L','XL','XXL'순서로")
def ShirtSize_num(ShirtSize):
    size_counter = [0 for _ in range(6)]
    for ss in ShirtSize:
        if(ss == "XS"):
            size_counter[0] += 1
        if(ss == "S"):
            size_counter[1] += 1
        if(ss == "M"):
            size_counter[2] += 1
        if(ss == "L"):
            size_counter[3] += 1
        if(ss == "XL"):
            size_counter[4] += 1
        if(ss == "XXL"):
            size_counter[5] += 1
    return size_counter


ShirtSize = []
for i in range(6):
    ShirtSize.append(input())
print(ShirtSize_num(ShirtSize))

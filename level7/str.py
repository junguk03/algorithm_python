def solution(s):
    s = s.replace(" ",",")
    max1 = "max(" + s + ")"
    min1 = "min(" + s + ")"
    str1 = str(eval(min1)) + " " + str(eval(max1))
    return str1

print(solution("1 2 3 4"))
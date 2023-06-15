def func_a(month,day):
    month_list = [31,28,31,30,31,30,31,31,30,31,30,31]
    total = 0
    for i in range(month-1):
        total += month_list[i]
    total += day
    return total-1

def solution(end_month,end_day):
    end_total = func_a(end_month,end_day)
    return end_total

month = int(input())
day = int(input())
print(solution(month,day))
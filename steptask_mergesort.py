import math


def merge(number_set_fst, number_set_sec):
    global ans
    number_set_res = []
    fst_len = len(number_set_fst)
    sec_len = len(number_set_sec)
    fst_index = 0
    sec_index = 0

    tasker = sec_len
    while fst_index != fst_len and sec_index != sec_len:
        if number_set_fst[fst_index] <= number_set_sec[sec_index]:
            number_set_res.append(number_set_fst[fst_index])
            fst_index += 1
        else:
            number_set_res.append(number_set_sec[sec_index])
            sec_index += 1
            ans += tasker - fst_index

    if fst_index != fst_len:
        for number in number_set_fst[fst_index:]:
            number_set_res.append(number)
    elif sec_index != sec_len:
        for number in number_set_sec[sec_index:]:
            number_set_res.append(number)

    return number_set_res


def iterative_merge_sort(number_set):
    queue = number_set
    iterative_index = 0

    while len(queue) != 2*length-1:
        queue.append(merge(queue[iterative_index], queue[iterative_index+1]))
        iterative_index += 2

    return queue[2*n-2]


n = int(input())
length = 2**(math.ceil(math.log2(n)))
a = [[int(i)] for i in input().split()]
ans = 0

a = [[-1] for i in range(n, length)] + a

iterative_merge_sort(a)
print(ans)

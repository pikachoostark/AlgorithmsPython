from math import floor

number_set = [int(i) for i in input().split()]
question_set = [int(i) for i in input().split()]
num_set_length = number_set.pop(0)
que_set_length = question_set.pop(0)
number_set.sort()


def binary_search(num, set_for_search=number_set):
    global num_set_length
    l = 0
    r = num_set_length-1
    while l <= r:
        m = floor((l + r) / 2)
        if set_for_search[m] == num:
            return m+1
        elif set_for_search[m] > num:
            r = m-1
        else:
            l = m+1
    return -1


for i in question_set:
    print(binary_search(i), end=' ')

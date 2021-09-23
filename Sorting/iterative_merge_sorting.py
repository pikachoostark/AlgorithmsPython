def merge(number_set_fst, number_set_sec):
    number_set_res = []

    while len(number_set_fst) != 0 and len(number_set_sec) != 0:
        if number_set_fst[0] < number_set_sec[0]:
            number_set_res.append(number_set_fst.pop(0))
        else:
            number_set_res.append(number_set_sec.pop(0))

    if len(number_set_fst) != 0:
        for number in number_set_fst:
            number_set_res.append(number)
    elif len(number_set_sec) != 0:
        for number in number_set_sec:
            number_set_res.append(number)

    return number_set_res


def iterative_merge_sort(number_set):
    queue = []

    for number in number_set:
        queue.append([number])

    while len(queue) != 1:
        queue.append(merge(queue.pop(0), queue.pop(0)))

    return queue.pop(0)


n = int(input())
a = [int(i) for i in input().split()]

print(iterative_merge_sort(a))

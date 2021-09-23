def calc(number):
    dict_list = {1: 0}
    prev_list = [1]
    curr_list = []
    ans = 0
    while number not in dict_list:
        for i in prev_list:
            if i * 3 <= number and i * 3 not in dict_list:
                dict_list[i * 3] = (ans + 1, i)
                curr_list.append(i * 3)
            if i * 2 <= number and i * 2 not in dict_list:
                dict_list[i * 2] = (ans + 1, i)
                curr_list.append(i * 2)
            if i + 1 <= number and i + 1 not in dict_list:
                dict_list[i + 1] = (ans + 1, i)
                curr_list.append(i + 1)
        prev_list = curr_list.copy()
        curr_list = []
        ans += 1

    ans_list = []
    index = number
    if number == 1:
        return 0, [1]
    for _ in range(dict_list[n][0]+1):
        if index == 1:
            ans_list.append(index)
            break
        else:
            ans_list.append(index)
            index = dict_list[index][1]
    return dict_list[n][0], ans_list


n = int(input())
printer = calc(n)
print(printer[0])
for i in sorted(printer[1]):
    print(i, end=' ')

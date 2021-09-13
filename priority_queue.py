from math import floor
priority_queue = list()


def insert(num, priority_queue=priority_queue):
    priority_queue.append(num)
    index_counter = len(priority_queue)
    while (floor(index_counter / 2) != 0) and (priority_queue[floor(index_counter / 2) - 1] < num):
        ind_parent = floor(index_counter / 2)
        priority_queue[index_counter-1] = priority_queue[ind_parent-1]
        priority_queue[ind_parent-1] = num
        index_counter = ind_parent


def extract_max(priority_queue=priority_queue):
    index_counter = 1
    while ((index_counter * 2) + 1) <= len(priority_queue):
        if priority_queue[index_counter * 2 - 1] >= priority_queue[index_counter * 2]:
            minimum_index = index_counter * 2
        else:
            minimum_index = index_counter * 2 + 1
        priority_queue[index_counter - 1], priority_queue[minimum_index - 1] = priority_queue[minimum_index - 1], \
                                                                               priority_queue[index_counter - 1]
        index_counter = minimum_index
    if (index_counter * 2) == len(priority_queue):
        minimum_index = index_counter * 2
        priority_queue[index_counter - 1], priority_queue[minimum_index - 1] = priority_queue[minimum_index - 1], \
                                                                               priority_queue[index_counter - 1]
        index_counter = minimum_index
    answer = priority_queue.pop(index_counter-1)
    return answer


command_count = int(input())
for _ in range(command_count):
    command = input()
    if command[0:6] == 'Insert':
        number = int(command[7:])
        insert(number)
        # print(priority_queue)
    elif command == 'ExtractMax':
        print(extract_max())
        # print(priority_queue)

def fibonacci_set(fib_index):
    fib_set = [0, 1]
    while fib_index > len(fib_set)-1:
        fib_set.append(fib_set[-2]+fib_set[-1])
    return fib_set[fib_index]


print(fibonacci_set(int(input("Введите номер числа в последовательности: "))))

def fibonacci_one(fib_index):
    a, b = 0, 1
    if fib_index == 0:
        return a
    elif fib_index == 1:
        return b
    else:
        while fib_index != 1:
            a, b = b, a+b
            fib_index -= 1
        return b


# TODO... Можно сделать поменьше строк и проверок в условном операторе
print(fibonacci_one(int(input("Введите номер числа в последовательности: "))))

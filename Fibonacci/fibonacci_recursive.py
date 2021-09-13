def fibonacci_recursive(fib_index):
    if fib_index == 0:
        return 0
    elif fib_index == 1:
        return 1
    else:
        return fibonacci_recursive(fib_index-1) + fibonacci_recursive(fib_index-2)


print(fibonacci_recursive(int(input("Введите номер числа в последовательности: "))))

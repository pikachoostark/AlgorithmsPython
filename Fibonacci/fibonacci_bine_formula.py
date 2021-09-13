def fibonacci_bine(n):
    sqrt5 = 5 ** 0.5
    phi = (1 + sqrt5) / 2
    psi = (1 + sqrt5) / 2
    return int((phi ** n - psi ** n) / sqrt5)


print(fibonacci_bine(int(input("Введите номер числа в последовательности: "))))

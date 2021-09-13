def gcd_euclid(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a

    if a >= b:
        return gcd_euclid(a % b, b)
    else:
        return gcd_euclid(a, b % a)


a, b = [int(i) for i in input("Введите два числа: ").split()]
print(gcd_euclid(a, b))

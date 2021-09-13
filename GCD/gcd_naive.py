def gcd_naive(a, b):
    gcd = 1

    if a > b:
        a, b = b, a

    for d in range(2, max(a, b)):
        if (a % d) and (b % d):
            gcd = d
    
    return gcd


a, b = [int(i) for i in input("Введите два числа: ").split()]
print(gcd_naive(a, b))

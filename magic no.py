

for n in range(1, 100):
    num = n

    while num > 9:
        k2 = 0

        while num != 0:
            k1 = num % 10
            num = num // 10
            k2 = k2 + k1

        num = k2

    if num == 1:
        print("Magic no. =", n)
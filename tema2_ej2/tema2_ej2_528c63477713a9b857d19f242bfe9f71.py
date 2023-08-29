def amigos(a, b):
    x = 1
    divisores_a = []
    divisores_b = []
    while x != 0:
        a = a
        rango_a = range(1, a)
        for x in rango_a:
            if a % x == 0:
                print("x: ", x)
                divisores_a.append(x)
                print("divisores_a: ", divisores_a)
                x = x + 1

            elif a % x != 0:
                x = x + 1

            print("suma divisores_a: ", sum(divisores_a))

        b = b
        i = 1
        while i != 0:
            rango_b = range(1, b)
            for i in rango_b:
                if b % i == 0:
                    print("i: ", i)
                    divisores_b.append(i)
                    print("divisores_b: ", divisores_b)
                    i = i + 1

                elif b % i != 0:
                    i = i + 1

                print("suma divisores_b: ", sum(divisores_b))

            if sum(divisores_a) == b or sum(divisores_b) == a and a != 1 and b != 2:

                return True
            else:
                return False

print(amigos(1, 2))
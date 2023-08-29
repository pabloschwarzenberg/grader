numero = int(input())
factor = 2
while factor <= numero:
        if not (numero % factor != 0):
            print(factor)
            numero /= factor
        factor += 1
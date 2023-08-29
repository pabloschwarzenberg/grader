def factorizar(numero):
    i = 2
    while i * i <= numero:
        if numero % i:
            i += 1
        else:
            numero //= i
            print(i)
    if numero > 1:
        print(numero)
numero = int(input())
factorizar(numero)

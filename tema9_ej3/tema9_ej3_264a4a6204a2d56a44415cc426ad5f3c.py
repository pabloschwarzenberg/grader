def descomponer(numero):
    f_primos = []
    for i in range(2, numero):
        while numero % i == 0:
            numero = numero / i
            f_primos.append(i)
    for a in range (len(f_primos)):
        print(f_primos[a], end='\n')
    print()
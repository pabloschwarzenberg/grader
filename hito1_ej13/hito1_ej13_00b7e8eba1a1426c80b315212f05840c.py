def factorizar(numero):
    factores_primos = []
    
    factor = 2
    
    while factor <= numero:
        if numero % factor == 0:
            factores_primos.append(factor)
            numero = numero / factor
        else:
            if factor == 2:
                factor = 3
            else:
                factor += 2
    
    for factor in factores_primos:
        print(factor)

numero = int(input("Ingrese un número entero: "))

factorizar(numero)
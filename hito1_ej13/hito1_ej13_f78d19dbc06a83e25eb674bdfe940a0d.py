def obtener_factores_primos(numero):
    factores = []

    # Comprobación de divisibilidad por 2
    while numero % 2 == 0:
        factores.append(2)
        numero = numero // 2

    # Comprobación de divisibilidad por números impares
    i = 3
    while i * i <= numero:
        while numero % i == 0:
            factores.append(i)
            numero = numero // i
        i += 2

    # Si el número restante es mayor que 2, es un factor primo
    if numero > 2:
        factores.append(numero)

    return factores


numero = int(input())

factores_primos = obtener_factores_primos(numero)

for factor in factores_primos:
    print(factor)
      
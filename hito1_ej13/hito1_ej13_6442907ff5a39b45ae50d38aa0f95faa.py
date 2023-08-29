def descomposicion_factores_primos(numero):
    for i in range(2, numero // 2 + 1):
        while numero % i == 0:
            print(i)
            numero //= i

    if numero > 1:
        print(numero)


num = int(input("Ingresa un número entero: "))
print("La descomposición de factores primos del número", num, "es:")
descomposicion_factores_primos(num)

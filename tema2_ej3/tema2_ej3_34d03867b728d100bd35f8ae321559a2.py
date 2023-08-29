def numero_perfecto(numero):
    suma_divisores = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma_divisores += i
    return suma_divisores == numero

    numero = int(input("Ingrese un número: "))
    es_perfecto = numero_perfecto(numero)
    if es_perfecto:
        print("El número {} es un número perfecto.".format(numero))
    else:
        print("El número {} no es un número perfecto.".format(numero))
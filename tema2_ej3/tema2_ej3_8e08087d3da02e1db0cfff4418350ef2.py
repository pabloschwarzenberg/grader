def numero_perfecto(numero):
    suma = 0
    for divisor in range(1, numero):
        if numero % divisor == 0:
            suma += divisor
    
    if suma == numero:
        return True
    else:
        return False

if __name__ == "__main__":
    # Solicitar al usuario un número entero
    numero = int(input("Ingrese un número entero: "))

    # Verificar si el número es perfecto
    es_perfecto = numero_perfecto(numero)

    # Imprimir el resultado
    if es_perfecto:
        print(numero, "es un número perfecto.")
    else:
        print(numero, "no es un número perfecto.")


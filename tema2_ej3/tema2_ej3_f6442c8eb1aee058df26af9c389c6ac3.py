def numero_perfecto(numero):
    # Verificar si el número es negativo o cero
    if numero <= 0:
        return False

    # Calcular la suma de los divisores
    suma = 0
    for divisor in range(1, numero):
        if numero % divisor == 0:
            suma += divisor

    # Determinar si el número es perfecto
    if suma == numero:
        return True
    else:
        return False

if __name__ == "__main__":
    # Solicitar al usuario que ingrese un número entero
    numero = int(input("Ingresa un número entero positivo: "))

    # Llamar a la función para determinar si es un número perfecto
    es_perfecto = numero_perfecto(numero)

    if es_perfecto:
        print(numero, "es un número perfecto.")
    else:
        print(numero, "no es un número perfecto.")

           
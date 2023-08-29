def numero_perfecto(numero):
    suma = 0

    # Calcular la suma de los divisores
    for i in range(1, numero):
        if numero % i == 0:
            suma += i

    # Verificar si el número es perfecto
    if suma == numero:
        return True
    else:
        return False
if __name__ == "__main__":
    # Solicitar al usuario ingresar el número
    numero = int(input("Ingrese un número: "))

    # Llamar a la función para verificar si es un número perfecto
    es_perfecto = numero_perfecto(numero)

    # Imprimir el resultado
    if es_perfecto:
        print("El número es perfecto.")
    else:
        print("El número no es perfecto.")
           
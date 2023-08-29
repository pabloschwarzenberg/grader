def numero_perfecto(numero):
    suma_divisores = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma_divisores += i
    if suma_divisores == numero:
        return True  # El número es perfecto
    else:
        return False  # El número no es perfecto

if __name__ == "__main__":
    numero = int(input("Ingrese un número: "))
    es_perfecto = numero_perfecto(numero)
    if es_perfecto:
        print(numero, "es un número perfecto.")
    else:
        print(numero, "no es un número perfecto.") 
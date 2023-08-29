def numero_perfecto(numero):
    suma_divisores = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma_divisores += i

    if suma_divisores == numero:
        return True
    else:
        return False

if __name__ == "__main__":
    num = int(input("Ingrese un número: "))
    es_perfecto = numero_perfecto(num)
    if es_perfecto:
        print("El número es perfecto")
    else:
        print("El número no es perfecto")
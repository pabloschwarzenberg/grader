def suma_divisores(numero):
    suma = 0

    for i in range(1, numero):
        if numero % i == 0:
            suma += i

    if suma == 1:
        return suma, True
    else:
        return suma, False

if __name__ == "__main__":
    num = int(input("Ingresa un número: "))
    resultado = suma_divisores(num)
    print("La suma de los divisores de", num, "es:", resultado[0])
    print("El número", num, "es primo:", resultado[1])

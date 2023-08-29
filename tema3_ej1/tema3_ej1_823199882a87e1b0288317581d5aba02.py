def suma_divisores(a):
    suma = 0
    for i in range(1, a):
        if a % i == 0:
            suma += i

    if suma == 1:
        return suma, True  # El número es primo
    else:
        return suma, False  # El número no es primo

if __name__ == "__main__":
    numero_ingresado = int(input("Ingresa un número: "))
    resultado, es_primo = suma_divisores(numero_ingresado)

    print("La suma de los divisores de", numero_ingresado, "es:", resultado)
    print("El número", numero_ingresado, "es primo:", es_primo)

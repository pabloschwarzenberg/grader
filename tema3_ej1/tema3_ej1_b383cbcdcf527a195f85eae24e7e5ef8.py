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
    numero = int(input("Ingrese un numero: "))
    resultado, es_primo = suma_divisores(numero)
    print("Suma de los divisores:", resultado)
    print("Es primo:", es_primo)
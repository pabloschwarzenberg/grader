# completa el código de la función
def suma_divisores(numero):
    suma = 0
    for divisor in range(1, numero):
        if numero % divisor == 0:
            suma += divisor

    if suma == 1:
        return suma, True  # El número es primo
    else:
        return suma, False  # El número no es primo

if __name__ == "__main__":
    numero = int(input("Ingrese un número: "))
    resultado = suma_divisores(numero)
    print("Suma de divisores:", resultado[0])
    print("Es primo:", resultado[1])

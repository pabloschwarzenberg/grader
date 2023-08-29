def suma_divisores(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    if suma == 1:
        return suma, True  # Es primo
    else:
        return suma, False  # No es primo


if __name__ == "__main__":
    numero = int(input("Ingrese un número: "))
    resultado, es_primo = suma_divisores(numero)
    print("La suma de los divisores es:", resultado)
    if es_primo:
        print("El número es primo.")
    else:
        print("El número no es primo.")


 

           
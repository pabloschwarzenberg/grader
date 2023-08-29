# completa el código de la función

def suma_divisores(número):
    suma = 0
    for i in range(1, número):
        if número % i == 0:
            suma += i

    if suma == 1:
        return suma, True ## Primo
    else:
        return suma, False ## No es primo

## Código para probar función

if __name__ == "__main__":
    número = int(input("Ingresa un número: "))
    Resultado, Es_Primo = suma_divisores(número)
    print("La suma de los divisores es:", Resultado)

    if Es_Primo:
        print("El número es primo")
    else:
        print("El número no es primo")
           
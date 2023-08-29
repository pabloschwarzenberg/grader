# completa el código de la función
def suma_divisores(numero):
    suma = 0

    # Ciclo para encontrar los divisores del número
    for i in range(1, numero):
        if numero % i == 0:
            suma += i

    # Verificar si la suma de los divisores es igual a 1
    if suma == 1:
        return suma, True  # El número es primo
    else:
        return suma, False  # El número no es primo

# Ejemplo de uso
if __name__ == "__main__":
    numero = int(input("Ingrese un número: "))
    suma, es_primo = suma_divisores(numero)
    print("La suma de los divisores de", numero, "es", suma)
    if es_primo:
        print(numero, "es primo")
    else:
        print(numero, "no es primo")
           
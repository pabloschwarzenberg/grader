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
    # Solicitar al usuario un número entero
    numero = int(input("Ingrese un número entero: "))

    # Calcular la suma de los divisores y verificar si el número es primo
    suma, es_primo = suma_divisores(numero)

    # Imprimir los resultados
    print("La suma de los divisores de", numero, "es:", suma)
    if es_primo:
        print(numero, "es un número primo.")
    else:
        print(numero, "no es un número primo.")

           
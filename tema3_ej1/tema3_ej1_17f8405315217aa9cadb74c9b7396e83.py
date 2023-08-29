# completa el código de la función
def suma_divisores(numero):
    suma = 0

    # Calcular la suma de los divisores
    for i in range(1, numero):
        if numero % i == 0:
            suma += i

    # Verificar si el número es primo
    es_primo = suma == 1

    return suma, es_primo

if __name__ == "__main__":
    # Solicitar el número al usuario
    numero = int(input("Ingrese un número: "))

    # Calcular la suma de los divisores y verificar si es primo
    resultado, es_primo = suma_divisores(numero)

    # Imprimir los resultados
    print("La suma de los divisores de", numero, "es:", resultado)
    print("El número", numero, "es primo:", es_primo)

           
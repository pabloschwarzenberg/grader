from os import system
system ("cls")
def suma_divisores(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i

    if suma == 1:
        return suma, True
    else:
        return suma, False

# Ejemplo de uso
if __name__ == "__main__":
    num = int(input("Ingrese un número: "))
    resultado, es_primo = suma_divisores(num)
    print("La suma de los divisores de", num, "es:", resultado)
    print("El número", num, "es primo:", es_primo)

           
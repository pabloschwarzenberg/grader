# completa el código de la función
def suma_divisores(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    return suma, suma == 1


if __name__ == "__main__":
    num = int(input("Ingrese un número: "))
    divisores, es_primo = suma_divisores(num)
    print("La suma de los divisores de", num, "es:", divisores)
    
    if es_primo:
        print(num, "es un número primo.")
    else:
        print(num, "no es un número primo.")


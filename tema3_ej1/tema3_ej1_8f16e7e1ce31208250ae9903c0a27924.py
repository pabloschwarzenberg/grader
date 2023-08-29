# completa el código de la función
def suma_divisores(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    if suma == 1:
        return (suma, True)
    else:
        return (suma, False)

if __name__ == "__main__":
    numero = int(input("Ingrese un número: "))
    resultado = suma_divisores(numero)
    print("La suma de los divisores de {} es {}.".format(numero, resultado[0]))
    if resultado[1]:
        print("{} es un número primo.".format(numero))
    else:
        print("{} no es un número primo.".format(numero))

           
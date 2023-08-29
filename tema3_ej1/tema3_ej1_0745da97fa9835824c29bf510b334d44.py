# completa el código de la función
def suma_divisores(num):
    suma = 0
    for i in range(1, num):
        if num % i == 0:
            suma += i
    primo = suma == 1
    return (suma, primo)
if __name__ == "__main__":
    num = int(input("Ingrese un número: "))
    resultado = suma_divisores(num)
    print("La suma de los divisores de {} es {}.".format(num, resultado[0]))
    if resultado[1]:
        print("{} es primo.".format(num))
    else:
        print("{} no es primo.".format(num))           
# completa el código de la función
def suma_divisores(a):
  return
def suma_divisores(numero):
    suma = 0
    for divisor in range(1, numero):
        if numero % divisor == 0:
            suma += divisor

    if suma == 1:
        return suma, True  # Es primo
    else:
        return suma, False  # No es primo

if __name__ == "__main__":
    num = int(input("Ingresa un número: "))
    suma, primo = suma_divisores(num)
    print("La suma de los divisores es:", suma)
    if primo:
        print("El número es primo")
    else:
        print("El número no es primo")
           
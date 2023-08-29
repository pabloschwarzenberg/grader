# completa el código de la función
def suma_divisores(a):
  return
           def suma_divisores(numero):
    suma = 0
    for divisor in range(1, numero):
        if numero % divisor == 0:
            suma += divisor
    if suma == 1:
        return suma, True  # número primo
    else:
        return suma, False  # número no primo

if __name__ == "__main__":
    numero = int(input("Ingrese un número: "))
    suma, es_primo = suma_divisores(numero)
    print("Suma de los divisores:", suma)
    if es_primo:
        print("El número es primo.")
    else:
        print("El número no es primo.")

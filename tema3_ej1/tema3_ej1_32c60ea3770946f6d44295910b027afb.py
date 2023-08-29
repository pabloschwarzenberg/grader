# completa el código de la función
def suma_divisores(a):
  return
def suma_divisores(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i

    if suma == 1:
        return suma, True  # El número es primo
    else:
        return suma, False  # El número no es primo

if __name__ == "__main__":
    # Solicitar al usuario ingresar el número
    numero = int(input("Ingrese un número: "))

    # Calcular la suma de los divisores y verificar si es primo
    resultado, es_primo = suma_divisores(numero)

    # Imprimir el resultado
    print("Suma de divisores:", resultado)
    print("Es primo:", es_primo)

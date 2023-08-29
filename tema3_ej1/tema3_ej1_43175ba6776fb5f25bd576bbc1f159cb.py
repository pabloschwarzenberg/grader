# completa el código de la función
def suma_divisores(a):
  return

def suma_divisores(numero):
    suma = 0
    es_primo = True
    # Calcular la suma de los divisores
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    # Determinar si el número es primo
    if suma != 1:
        es_primo = False
    return suma, es_primo


if __name__ == "__main__":
    # Solicitar al usuario ingresar el número
    numero = int(input("Ingrese un número: "))

    # Llamar a la función para obtener la suma de los divisores y si es primo o no
    suma, primo = suma_divisores(numero)

    # Imprimir el resultado
    print("Suma de los divisores:", suma)
    if primo:
        print("El número es primo.")
    else:
        print("El número no es primo.")
# completa el código de la función
def suma_divisores(a):
  return
def suma_divisores(numero):
    suma = sum(i for i in range(1, numero) if numero % i == 0)
    es_primo = suma == 1
    return suma, es_primo

if __name__ == "__main__":
    numero = int(input("Ingresa un número: "))
    suma, es_primo = suma_divisores(numero)

    print("La suma de los divisores de", numero, "es:", suma)

    if es_primo:
        print(numero, "es un número primo.")
    else:
        print(numero, "no es un número primo.")
           
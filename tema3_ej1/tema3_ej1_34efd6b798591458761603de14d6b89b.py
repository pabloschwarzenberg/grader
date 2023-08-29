# completa el código de la función
def suma_divisores(a):
  return
def suma_divisores(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    
    es_primo = suma == 1

    return suma, es_primo

if __name__ == "__main__":
    numero = int(input("Ingresa un número: "))
    divisores, es_primo = suma_divisores(numero)
    print("La suma de los divisores de", numero, "es:", divisores)
    print("El número", numero, "es primo:", es_primo)
           
#Factores Primos
def descomposicion_factores_primos(numero):
    factor = 2

    while factor <= numero:
        if numero % factor == 0:
            print(factor)
            numero = numero // factor
        else:
            factor += 1

numero = int(input())

descomposicion_factores_primos(numero)
      
16.# completa el código de la función
def suma_divisores(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    if suma == 1:
        return suma, True
    else:
        return suma, False
if __name__ == "__main__":
    numero = int(input("Ingresa un número: "))
    resultado, es_primo = suma_divisores(numero)
    print("La suma de los divisores de", numero, "es:", resultado)
    if es_primo:
        print(numero, "es un número primo.")
    else:
        print(numero, "no es un número primo.") 
      
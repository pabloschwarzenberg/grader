# completa el código de la función
def suma_divisores(numero):
    suma = 0
    # Iterar desde 1 hasta (numero-1)
    for i in range(1, numero):
        # Si el número es divisible por i, agregar i a la suma
        if numero % i == 0:
            suma += i
    # Determinar si el número es primo o no
    es_primo = suma == 1
    # Retornar la suma de los divisores y si el número es primo
    return suma, es_primo
if __name__ == "__main__":
    numero=eval(input("Ingrese su numero: "))
    if numero_perfecto(numero):
        print("El numero {0} es perfecto".format(numero))
    else:
        print("El numero {0} no es perfecto".format(numero))
           
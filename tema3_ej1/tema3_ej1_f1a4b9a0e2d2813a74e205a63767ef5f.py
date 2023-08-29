# completa el código de la función
def suma_divisores(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    
    es_primo = suma == 1
    
    return suma, es_primo

if __name__ == "__main__":
    numero = int(input("Ingrese un número: "))
    resultado = suma_divisores(numero)
    print("La suma de los divisores de", numero, "es", resultado[0])
    if resultado[1]:
        print(numero, "es un número primo.")
    else:
        print(numero, "no es un número primo.")

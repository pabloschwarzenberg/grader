# completa el código de la función
def suma_divisores(a):
    suma = 0
    for i in range(1, a):
        if (a % i == 0):
            suma += i
    
    if (suma == 1):
        es_primo = True
    else:
        es_primo = False
    
    return suma, es_primo

if __name__ == "__main__":
    a = int(input("Ingrese un número: "))
    resultado = suma_divisores(a)
    print("La suma de los divisores de", a, "es:", resultado[0])
    if resultado[1]:
        print(a, "es un número primo.")
    else:
        print(a, "no es un número primo.")
           
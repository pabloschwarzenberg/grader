# completa el código de la función
def suma_divisores(a):
    suma = 0
    for i in range(1, a):
        if a % i == 0:
            suma += i
    
    if suma == 1:
        return suma, True  # El número es primo
    else:
        return suma, False  # El número no es primo

if __name__ == "__main__":
    numero = int(input("Ingrese un número: "))
    suma = suma_divisores(numero)
    print("La suma de los divisores de", numero, "es", suma)
    
    if es_primo:
        print(numero, "es primo")
    else:
        print(numero, "no es primo")

           
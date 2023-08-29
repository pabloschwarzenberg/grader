# completa el código de la función
def suma_divisores(numero):
    suma = 0
    for divisor in range(1, numero):
        if numero % divisor == 0:
            suma += divisor
    
    return suma, suma == 1

def main():
    numero = int(input("Ingrese un número: "))
    
    suma, primo = suma_divisores(numero)
    print("La suma de los divisores es", suma)
    
    if primo:
        print("El número es primo")
    else:
        print("El número no es primo")

if __name__ == "__main__":
    main()

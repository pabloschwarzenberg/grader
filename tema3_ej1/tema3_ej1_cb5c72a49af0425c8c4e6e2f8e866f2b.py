# divisores

def suma_divisores(n):
    suma = 0
    primo = 0
    for i in range (1, n):
        if n % i == 0:
            suma = suma + i
    
    if suma == 1:
        primo = 1
    
    return [suma, primo]

if __name__ == "__main__":
    n = int(input("Ingrese un numero: "))
    result = suma_divisores(n)

    print("La suma de los divisores del numero ingresado es: " + str(result[0]))
    if result[1] == 1:
        print("El numero ingresado es primo")
    else:
        print("El numero ingresado no es primo")

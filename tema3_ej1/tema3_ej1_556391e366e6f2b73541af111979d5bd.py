# completa el código de la función
def suma_divisores(a):
    suma = 0
    for i in range(1, a):
        if a % i == 0:
            suma += i
    
    return suma, suma == 1

if __name__ == "__main__":
    num = int(input("Ingrese un número: "))
    suma, es_primo = suma_divisores(num)
    print("La suma de los divisores es:", suma)
    
    if es_primo:
        print("El número es primo.")
    else:
        print("El número no es primo.")
           
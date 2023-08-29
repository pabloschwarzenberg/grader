# completa el código de la función
def suma_divisores(a):
    suma = 0
    for i in range(1, a):
        if a % i == 0:
            suma += i
    
    es_primo = (suma == 1)
    
    return suma, es_primo

if __name__ == "__main__":
    num = int(input("Ingrese un número: "))
    suma, es_primo = suma_divisores(num)
    
    print("La suma de los divisores de", num, "es:", suma)
    if es_primo:
        print(num, "es primo.")
    else:
        print(num, "no es primo.")
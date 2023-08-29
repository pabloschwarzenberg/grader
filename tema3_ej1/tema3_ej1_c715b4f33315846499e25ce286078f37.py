def suma_divisores(numero):
    suma = 0
    
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    
    es_primo = suma == 1
    
    return suma, es_primo


if __name__ == "__main__":
    num = int(input("Ingrese un número: "))
    divisores_suma, es_primo = suma_divisores(num)
    print("Suma de los divisores:", divisores_suma)
    
    if es_primo:
        print("El número es primo.")
    else:
        print("El número no es primo.")

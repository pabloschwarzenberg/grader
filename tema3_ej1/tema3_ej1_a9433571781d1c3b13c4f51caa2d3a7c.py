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
    numero_ingresado = int(input("Ingrese un número: "))
    resultado_suma, es_primo = suma_divisores(numero_ingresado)
    
    print("La suma de los divisores de", numero_ingresado, "es:", resultado_suma)
    print("El número", numero_ingresado, "es primo?", es_primo)
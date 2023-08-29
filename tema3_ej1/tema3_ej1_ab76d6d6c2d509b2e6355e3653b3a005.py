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

    numero = 10
    resultado, es_primo = suma_divisores(numero)
    print("Suma de los divisores de", numero, ":", resultado)
    print("¿El número", numero, "es primo?:", es_primo)

    numero = 13
    resultado, es_primo = suma_divisores(numero)
    print("Suma de los divisores de", numero, ":", resultado)
    print("¿El número", numero, "es primo?:", es_primo)

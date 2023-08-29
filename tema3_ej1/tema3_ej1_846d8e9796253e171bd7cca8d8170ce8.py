# completa el código de la función
def suma_divisores(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    
    es_primo = suma == 1
    
    return suma, es_primo
if __name__ == "__main__":
    num = 12
    divisores, primo = suma_divisores(num)
    print("Suma de los divisores de", num, ":", divisores)
    print(num, "es primo?" if primo else num, "no es primo")

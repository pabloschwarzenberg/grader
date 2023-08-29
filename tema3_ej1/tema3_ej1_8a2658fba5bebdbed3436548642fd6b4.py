def suma_divisores(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i

    if suma == 1:
        return True  
    else:
        return False  
if __name__ == "__main__":
    numero = int(input("Ingrese un número: "))
    es_primo = suma_divisores(numero)

    if es_primo:
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")

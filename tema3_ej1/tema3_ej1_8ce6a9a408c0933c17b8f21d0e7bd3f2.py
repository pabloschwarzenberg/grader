def suma_divisores(a):
    suma = 0
    for i in range(1, a):
        if a % i == 0:
            suma += i
    
    if suma == 1:
        return suma, True
    else:
        return suma, False

if __name__ == "__main__":
    numero = int(input("Ingrese un número: "))
    resultado, es_primo = suma_divisores(numero)
    print("La suma de los divisores de", numero, "es:", resultado)
    if es_primo:
        print(numero, "es un número primo.")
    else:
        print(numero, "no es un número primo.")
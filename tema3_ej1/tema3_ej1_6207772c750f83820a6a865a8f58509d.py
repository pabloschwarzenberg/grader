# completa el código de la función
def suma_divisores(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    if suma == 1:
        return suma, True  # El número es primo
    else:
        return suma, False  # El número no es primo

if __name__ == "__main__":
    numero_ingresado = int(input("Ingrese un número: "))
    suma, es_primo = suma_divisores(numero_ingresado)
    print("La suma de los divisores de", numero_ingresado, "es:", suma)
    print("¿El número", numero_ingresado, "es primo?", es_primo)
           
if __name__ == "__main__":
    numero = int(input("Ingrese un número: "))
    suma, primo = suma_divisores(numero)

    print("La suma de los divisores de", numero, "es:", suma)
    print("¿Es primo?", primo)

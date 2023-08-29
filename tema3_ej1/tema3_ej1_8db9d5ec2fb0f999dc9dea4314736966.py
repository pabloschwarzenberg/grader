def suma_divisores(numero):
    suma = sum(i for i in range(1, numero) if numero % i == 0)
    es_primo = suma == 1
    return suma, es_primo

if __name__ == "__main__":
    numero = int(input("Ingrese un número: "))
    resultado, primo = suma_divisores(numero)
    print("Suma de divisores:", resultado)
    print("El número es primo:", primo)
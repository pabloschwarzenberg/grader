python
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
    numero = 7
    suma, es_primo = suma_divisores(numero)
    print(f"La suma de los divisores de {numero} es {suma}. ¿Es un número perfecto? {es_primo}")
           
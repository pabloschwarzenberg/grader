def numero_perfecto(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    return suma == numero

if __name__ == "__main__":
    numero = int(input("Ingrese un número: "))
    es_perfecto = numero_perfecto(numero)
    print("Es perfecto:", es_perfecto)

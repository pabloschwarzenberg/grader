def numero_perfecto(a):
    suma_divisores = 0
    for i in range(1, a):
        if (a % i == 0):
            suma_divisores += i
    return suma_divisores == a

if __name__ == "__main__":
    a = int(input("Ingrese un número: "))
    es_perfecto = numero_perfecto(a)
    print(es_perfecto)
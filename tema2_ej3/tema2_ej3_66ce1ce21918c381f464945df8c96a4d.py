a=int(input("Ingrese a: "))

def es_numero_perfecto(a):
    suma = 0

    for i in range(1, a):
        if a % 1 == 0:
            suma += i

    return suma == a

print(es_numero_perfecto(a))
           
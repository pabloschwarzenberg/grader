def numero_perfecto(x):
    suma_numeros = 0

    for i in range(1,x):
        if x % i == 0:
            suma_numeros += i
    return suma_numeros == x

if "_name_" == "_main_":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(x))
           
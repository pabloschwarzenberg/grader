def numero_perfecto(n):
    divisores = []
    for i in range(1, n):
        if n%i == 0:
            i = divisores.append(i)

    suma = 0
    for divisor in divisores:
        suma = suma + divisor
    if suma == n:
        esPerfecto = True
    else:
        esPerfecto = False
    return esPerfecto
if __name__=="main_":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))           
def numero_perfecto(a):
    divisores = []
    for i in range(1, a):
        if a%i == 0:
            i = divisores.append(i)
    suma = 0
    for divisor in divisores:
        suma = (suma + divisor)
    if suma == a:
        esPerfecto = True
    else:
        esPerfecto = False
    return esPerfecto
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
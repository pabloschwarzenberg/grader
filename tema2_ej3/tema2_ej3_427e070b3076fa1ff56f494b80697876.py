def numero_perfecto(r):
    divisores = []
    for i in range(1, r):
        if r%i == 0:
            i = divisores.append(i)

    suma = 0
    for divisor in divisores:
        suma = suma + divisor
    if suma == r:
        Perfecto = True
    else:
        Perfecto = False
    return Perfecto
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
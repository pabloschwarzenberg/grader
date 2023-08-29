def numero_perfecto(a):
    divisores = []
    divisor = 1
    suma = 0
    while divisor < a:
        dividido = a % divisor
        if dividido == 0:
            divisores.append(divisor)
            divisor = divisor + 1
        else:
            divisor = divisor + 1
    for i in range(0, len(divisores)):
        suma = suma + divisores[i]
    if suma == a:
        return (True)
    else:
        return (False)


if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           
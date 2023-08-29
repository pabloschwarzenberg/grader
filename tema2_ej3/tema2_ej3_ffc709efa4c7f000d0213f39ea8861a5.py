def numero_perfecto(n):
    div = []
    for i in range(1, n):
        if n%i == 0:
            i = div.append(i)
    
    ##sumar divisores
    suma = 0
    for divisor in div:
        suma = suma + divisor
    if suma == n:
        perfecto = True
    else:
        perfecto = False
    return perfecto
if __name__=="__main__":
    v=int(input("Ingresa v: "))
    print(numero_perfecto(v))
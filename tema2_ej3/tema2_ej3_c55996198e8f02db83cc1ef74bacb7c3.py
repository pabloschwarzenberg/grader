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
        esPerfecto = True
    else:
        esPerfecto = False
    return esPerfecto
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           
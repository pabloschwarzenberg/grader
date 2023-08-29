#def numero_perfecto(a):
#    return False

#if __name__=="__main__":
#    a=int(input("Ingrese a: "))
#    print(numero_perfecto(a))
#------------------------------------------
def numero_perfecto(n):
    Divisores = []
    for i in range(1, n):
        if n%i == 0:
            i = Divisores.append(i)
    
    ##sumar los divisores
    suma = 0
    for divisor in Divisores:
        suma = suma + divisor
    if suma == n:
        EsPerfecto = True
    else:
        EsPerfecto = False
    return EsPerfecto
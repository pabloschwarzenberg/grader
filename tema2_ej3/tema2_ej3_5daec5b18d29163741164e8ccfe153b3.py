def numero_perfecto(a):
    sumaDeDivisores = 0
    numeroPerfecto = True
    for numero in range(1, a):
        modulo = a % numero
        if (modulo == 0):
            sumaDeDivisores = sumaDeDivisores + numero
    if (sumaDeDivisores == a ):
        numeroPerfecto = True
    else:
        numeroPerfecto = False 
        
    return numeroPerfecto 

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
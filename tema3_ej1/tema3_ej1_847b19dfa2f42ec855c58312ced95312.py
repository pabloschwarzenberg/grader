# completa el código de la función
def suma_divisores(n):
    i=1
    suma =0
    while i<n:
        if n%i ==0:
            suma = suma+i
            i+=1
        else:
            i+=1
    if suma==1:
        return (suma, True)
    else:
        return (suma, False)
        

           
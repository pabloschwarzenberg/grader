# completa el código de la función
def suma_divisores(a):
    suma=0
    valor=1
    while valor<a:
        if a%valor==0:
            suma+=valor
        valor+=1
    return suma
def primo(a):
    global suma
    if a==1:
        return(0,False)
    elif suma==1:
        return(suma,True)
    else:
        return(suma,False)
    

           
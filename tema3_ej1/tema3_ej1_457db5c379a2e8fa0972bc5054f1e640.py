# completa el código de la función
def suma_divisores(a):
    suma=0
    contador=1
    while contador<a:
        if a%contador==0:
            suma+=contador
            contador+=1
        else:
            contador+=1
    if suma==1:
        return suma, True
    else:
        return suma, False
           
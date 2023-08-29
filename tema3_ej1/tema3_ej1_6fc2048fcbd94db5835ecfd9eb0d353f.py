# completa el código de la función
def suma_divisores(a):
    num = a
    suma=0
    for i in range(1,num):
        if num%i==0:
            suma=suma+i
    if suma==1:
        resultado = True
    else:
        resultado = False
    return suma, resultado

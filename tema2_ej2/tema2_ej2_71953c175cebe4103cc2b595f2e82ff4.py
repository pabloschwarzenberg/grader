# completa el código de la función
def amigos(a,b):
    suma=0
    #for i in range(1,(a+1)):
    for i in range(1, a):
        if a%i==0:
            suma=suma+i
    print(suma)
    #DOCENTE: Te faltó calcular la suma de los divisores del segundo numero
    suma2=0
    for i in range(1, b):
        if b%i==0:
            suma2=suma2+i
    print(suma2)
    #DOCENTE: ESTA NO ES LA CONDICION. A parte de que suma se igual al segundo nuúmero
    # la suma de los divisores del segundo numero debe ser igual al primero
    #if suma==b:
    if suma == b and suma2 == a:
            resultado=True
    else:
        #suma!=b
        resultado=False
    return resultado
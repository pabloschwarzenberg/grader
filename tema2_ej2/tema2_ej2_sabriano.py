# completa el código de la función
def amigos(a,b):
    numero=1
    divisores=[]
    while a>=numero:
        if a%numero==0:
            divisores.append(numero)
            numero=numero+1
        else:
            numero=numero+1
    suma=0
    for i in divisores:
        suma=suma+i
    numero1=1
    divisores1=[]
    while b>=numero1:
        if b%numero1==0:
            divisores1.append(numero1)
            numero1=numero1+1
        else:
            numero1=numero1+1
    suma1=0
    for i in divisores1:
        suma1=suma1+i
    if a==b:
        return False
    elif suma1==suma:
      return True
    else:
        return False
           
# completa el código de la función
def amigos(a,b):
    numero=0
    lista_a=[]
    sonamigos=True
    if a==b:
        return False
    if a==1 or b==1:
        return False
    divisor=1
    while divisor < a :
        if a%divisor==0:  
            numero=a//divisor
            if numero==a:
                numero=0
            else:
                numero=str(numero)
                lista_a.append(numero)
        divisor += 1
    lista_a.append(1)
    i=0
    suma=0
    while i <= len(lista_a)-1:
        numero=lista_a[i]
        numero=int(numero)
        suma=numero+suma
        i+=1
    if suma==b:
        return True
    else:
        return False
           
# completa el código de la función
def suma_divisores(a):
    lista=[]
    b=a-1
    while b>0:
        if a%b==0:
            lista.append(b)
            b=b-1
            continue
        else:
            b=b-1
            continue
    sumar=0
    for j in lista:
        sumar=sumar+j
    if sumar==1:
        return sumar,True
    if sumar!=1:
        return sumar,False

           
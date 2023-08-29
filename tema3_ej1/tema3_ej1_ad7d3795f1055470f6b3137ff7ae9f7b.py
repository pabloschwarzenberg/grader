# completa el código de la función
def suma_divisores(n):
    I=1
    suma=0

    while I<n:
        if n%I==0:
            suma=suma+I
        I=I+1
    if suma==1:
        es_primo=True
    else:
        es_primo=False 
    return suma,es_primo
r=suma_divisores(21)
print (r)



           
# completa el código de la función
def suma_divisores(a):
    i=1
    divisores = []
    while i < a:
        if a%i==0:
            divisores.append(i)
            i+=1
        else:
            i+=1
    suma_total=0
    for elem in divisores:
        suma_total+= elem
        
    if suma_total==1:
        booleano=True
    else:
        booleano=False
    return suma_total, booleano
           
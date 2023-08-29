# completa el código de la función
def primo(a):
    i=2
    primo=True
    while i<a:
        if a%i==0:
            primo=False
            break
        i+=1
    if primo and a!=1:
        return True
    else:
        return False
def divisores(a):
    i=1
    divisores=[]
    while i<a:
        if a%i==0:
           divisores.append(i)
        i+=1
    if a==1:
        return [0]
    return divisores
def suma_divisores(a):
    suma=0
    for i in divisores(a):
        suma=suma+i
    return suma, primo(a)

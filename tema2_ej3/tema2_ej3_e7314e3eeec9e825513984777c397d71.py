def suma_divisores(a):
    divisores_a=[]
    i=1
    while i<a:
        if a%i==0:
            divisores_a.append(i)
        i+=1
    largo=len(divisores_a)
    suma=0
    x=0
    while x<largo:
        suma+=divisores_a[x]
        x+=1
    return suma

def numero_perfecto(a):
    if suma_divisores(a)==a:
        return True
    else:
        return False
           
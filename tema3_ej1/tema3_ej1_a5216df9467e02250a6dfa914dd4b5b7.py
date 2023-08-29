# completa el código de la función
def suma_divisores(valor):
    divisores=[]
    suma=0
    for n in range(1,valor):
        if valor % n == 0:
            divisores.append(n)
            print(divisores)
    for q in divisores:
        if q == valor:
            divisores.remove(q)
            print(divisores)
    for s in divisores:
        suma +=s 
    if suma ==1:
        resultado= suma,True
        return resultado
    else:
        resultado= suma,False
        return resultado       
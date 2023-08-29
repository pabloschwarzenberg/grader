# completa el código de la función
def suma_divisores(n):
    divisores=[]
    k=1
    for k in range(1,(n+1)):
        if n%k==0:
            divisores.append(k)
        else:
            divisores=divisores
    divisores.pop()
    suma=0
    for i in range(len(divisores)):
        suma=suma+int(divisores[i])
    if suma==1 and n!=1:
        a=True
    else:
        a=False
    return suma,a
        
  
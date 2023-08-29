#Conversión de Decimal a Binario
def binario(n):
    lista=[]
    x=0
    y=1
    n=int(n)
    while n!=0:
        if (n%2==0):
            lista.append(x)
            n=n/2
            n=int(n)
        if (n%2==1):
            lista.append(y)
            n=n/2
            n=int(n)
    lista.reverse()
    lista=list(map(str,lista))
    res=''.join(lista)
    return res
n=float(input('ingrese numero decimal: '))
resultado=binario(n)  
print('resultado=',resultado)
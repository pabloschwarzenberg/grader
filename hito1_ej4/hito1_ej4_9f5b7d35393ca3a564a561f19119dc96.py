#Conversión de Decimal a Binario
nd=int(input('Ingrese su numero: '))
L=[]
while nd!=0:
    nb=nd%2
    nbs=str(nb)
    nd=nd//2
    L.append(nbs)
Ls=''.join(L)
Ls=Ls[::-1]
print('resultado='+Ls)
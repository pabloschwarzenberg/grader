texto=input()
rango=int(input())
combinaciones=[]
nuevas_c=[]
i=0
g=1
h=0
k=0

while i<(len(texto)):

    x=(texto[i:(rango+i)])
    combinaciones.append(x)
    i=i+1

combinaciones.pop(-1)
combinaciones.pop(-1)



while h<len(combinaciones):

    y=combinaciones.count(combinaciones[h])

    if y==1:
        z=str(combinaciones[h])
        nuevas_c.append(z)

    h=h+1

if len(nuevas_c)>0:
    print(nuevas_c)
elif len(nuevas_c)==0:
    print("ninguna")
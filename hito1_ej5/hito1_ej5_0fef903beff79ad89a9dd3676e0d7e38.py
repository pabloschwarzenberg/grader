numero=input("Ingrese el rut:")
largo= len(numero)

contador=1
sumador=0
for x in range (largo-1,-1,-1):
    contador=contador+1
    sumador=sumador + int(numero[x])*contador
    if contador==7:
        contador=1

resto=sumador%11

digitov=11-resto

digitov=str(digitov)
if digitov=="11":
    digitov="0"
if digitov=="10":
    digitov="K"
print("dv=",digitov)

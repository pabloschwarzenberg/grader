#Cálculo del dígito verificador de un rut
#posicion 01234567
numero = input('Ingrese el número:')
largo=len(numero)
print("\n")
contador=1
sumador = 0
for x in range(largo-1,-1,-1): #posiciones:(7,6,5,4,3,2,1)del numero="30686957"
    contador=contador + 1
    sumador= sumador + int(numero[x])*contador
    if(contador == 7):
        contador=1
#print(sumador)
resto = sumador%11
DV=11-resto
#print(resto)
DV = str(DV)
if DV=="11":
   DV="0"
if DV=="10":
   DV="K"
print("dv=", DV)
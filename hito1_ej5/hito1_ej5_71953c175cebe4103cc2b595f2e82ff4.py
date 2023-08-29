#Cálculo del dígito verificador de un rut
numero = input("Ingrese el número: ")
largo = len(numero) #8
print("\n")
contador = 1
sumador = 0
for x in range(largo-1,-1,-1): #posiciones:[7,6,5,4,3,2,1,0] de numero="30686957" 
    contador = contador + 1
    sumador = sumador + int(numero[x])*contador 
    if (contador == 7):
        contador = 1
#print(sumador)
resto = sumador%11
#print(resto)
DV = 11 - resto
#print(DV)
DV = str(DV)
if DV=="11":
   DV = "0"
if DV=="10":
   DV = "K"
print("dv=", DV)      
#Cálculo del dígito verificador de un rut
numero=input("ingrese parte numerica del rut:")
largo=len(numero)
print("\n")
contador=1
sumador=0

for x in range(largo-1,-1,-1):  
    contador=contador+1
    sumador= sumador+int(numero[x])*contador 
    if contador ==7:
        contador=1

resto=sumador%11
DV= 11-resto
DV=str(DV)
if DV==11:
    DV="0"
if DV==10:
    DV= "K"
print("DV=", DV)
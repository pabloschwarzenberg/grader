#Cálculo del dígito verificador de un rut
rut=input("ingrese un rut sin digito verificador: ")
largo=len(rut)
factores=[2,3,4,5,6,7,2,3]
lista=[]
for i in range(largo-1,-1,-1):
    lista.append(int(rut[i])*factores[largo-1-i])
suma=0
for i in lista:
    suma=suma+i
resto=suma%11
final=11-resto
dv=""
if final==11:
    dv="0"
elif final==10:
    dv="K"
else:
    dv=str(final)
print("dv=",dv)
      
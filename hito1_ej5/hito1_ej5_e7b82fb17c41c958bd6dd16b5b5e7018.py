#Cálculo del dígito verificador de un rut
numero=input("ingrese numero: ")
largo=len(numero)
x=1
y=0
for n in range(largo-1,-1,-1):
    x=x+1
    y=y+int(numero[n])*x
    
    if(x==7):
        x=1
sobrante=y%11
dv=11-sobrante
dv=str(dv)
if(dv=="11"):
    dv="0"
if(dv=="10"):
    dv="k"
print("dv=",dv)

      
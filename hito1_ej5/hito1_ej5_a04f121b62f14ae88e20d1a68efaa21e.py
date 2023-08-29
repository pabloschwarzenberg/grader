#Cálculo del dígito verificador de un rut
rut=input("Ingresa tu rut sin el dv")
multi=2
suma=0
prod=0
n=1
while n<=len(rut):
    if multi>7:
        multi=2
    prod=int(rut[-n])*multi
    suma=suma+prod
    n+=1
    multi+=1
guion=11-suma%11
if guion==10:
    print("dv=K")
elif guion==11:
    print("dv=0")
else:
    print("dv=",guion)

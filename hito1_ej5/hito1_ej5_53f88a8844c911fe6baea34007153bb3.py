#Cálculo del dígito verificador de un rut
rut = input("RUT sin verificador: ")
ruto=[]
suma=0
p=2
for n in rut:
    n=int(n)
    ruto.append(n)

ruto.reverse()
x=len(ruto)
for i in range(x):
    suma+=ruto[i]*p
    p=p+1
    if p==8:
        p=2

mod=suma%11
digito=11-mod

if digito==11:
    print("dv=0")
elif digito==10:
    print("dv=K")
else:
    print("dv=",digito)
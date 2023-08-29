rut=str(input("ingresa rut"))

tam=len(rut)
tam1=len(rut)

lista= rut[::-1]

c=0

while tam>0:
    b = int(lista[int(tam1)-int(tam)])  
    contador =int(tam1)-int(tam)
    
    if 5>=int(contador):
        j=b*(2+(contador))
        c=c+j
    else:
        j=b*(2+(contador-6))
        c=c+j
    tam = tam-1

t=c//11
t1=c-(t*11)

t2=11-t1
dv="dv="+str(t2)

if t2==11:
    print("dv=0")
if t2==10:
    print("dv=k")
elif t2!=11 and t2!=10:
    print(dv)
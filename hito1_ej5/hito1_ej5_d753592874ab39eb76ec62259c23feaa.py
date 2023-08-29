#Cálculo del dígito verificador de un rut
rut=str(input("Indique su rut: "))

p=int(rut)

p=rut[::-1]

q=2
suma=0
for i in p:
    a=int(i)
    b=a*q
    q+=1
    suma+=b
    if q>7:
        q-=6

b=suma//11

a=suma-(11*b)
w=11-a

if w==11:
    print("dv=","0")
elif w==10:
    print("dv=","k")
else:
    print("dv=", w)

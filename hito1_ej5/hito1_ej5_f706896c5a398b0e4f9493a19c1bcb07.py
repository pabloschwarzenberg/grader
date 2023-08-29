#Cálculo del dígito verificador de un rut
RUT=int(input("Ingrese tu RUT: "))
b=2
d=0
while RUT>0:
    a=RUT%10
    RUT=RUT//10
    c=a*b
    d=d+c
    if b==7:
        b=2
    else :
        b+=1
V=11-(d%11)
if V==10 :
    print("dv=k")
elif V==11:
    print("dv=0")
else :
    print("dv=", V)
 


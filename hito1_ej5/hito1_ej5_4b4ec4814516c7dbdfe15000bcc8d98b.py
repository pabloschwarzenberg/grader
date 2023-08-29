rut=str(input("Ingrese su RUT sin puntos: "))

if len(rut)==8:
    a=int(rut[0])
    b=int(rut[1])
    c=int(rut[2])
    d=int(rut[3])
    e=int(rut[4])
    f=int(rut[5])
    g=int(rut[6])
    h=int(rut[7])

else:
    a=0
    b=int(rut[0])
    c=int(rut[1])
    d=int(rut[2])
    e=int(rut[3])
    f=int(rut[4])
    g=int(rut[5])
    h=int(rut[6])

x=int((3*a)+(2*b)+(7*c)+(6*d)+(5*e)+(4*f)+(3*g)+(2*h))

y=int(x%11)

dv=11-y

if y==0:
     print("dv=0")
     
elif dv==10:
    print("dv=k")
    
else:
    print("dv=",dv)   
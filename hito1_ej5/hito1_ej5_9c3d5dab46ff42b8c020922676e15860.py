#Cálculo del dígito verificador de un rut
rut = int(input("Escriba su rut sin puntos,guion ni codigo verificacion: "))
c=((rut//1)%10)*2
a=((rut//10)%10)*3
m=((rut//100)%10)*4
n=((rut//1000)%10)*5
b=((rut//10000)%10)*6
v=((rut//100000)%10)*7
s=((rut//1000000)%10)*2
x=(rut//10000000)*3
Suma = (c+a+m+n+b+v+s+x)
Resto1 = Suma//11
Resto2 = Suma-(11*Resto1)
Resta = 11-Resto2
if Resta == 11:
    print("dv=",end="")
    print(0)
elif Resta == 10:
    print("dv=",end="")
    print("k")
else:
    print("dv=",end="")
    print(Resta)
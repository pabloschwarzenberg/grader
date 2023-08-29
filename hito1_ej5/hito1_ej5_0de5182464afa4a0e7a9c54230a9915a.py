#Cálculo del dígito verificador de un rut
rut= int(input("Ingrese su rut: "))
z=(rut//10000000)*3
x=((rut//1000000)%10)*2
c=((rut//100000)%10)*7
v=((rut//10000)%10)*6
b=((rut//1000)%10)*5
n=((rut//100)%10)*4
m=((rut//10)%10)*3
s=((rut//1)%10)*2
resultadorut =(z+x+c+v+b+n+m+s)
diferencia = resultadorut//11
resta = resultadorut-(11*diferencia)
resta1 = 11-resta
if resta1 == 11:
    print("dv=",end=" ")
    print("0")
elif resta1 == 10:
    print("dv=",end=" ")
    print("k")
else:
    print("dv=",end=" ")
    print(resta1)




rut=int(input("Ingrese el rut: "))
a=(rut//10000000) * 3
b=((rut//1000000)%10) * 2
c=((rut//100000)%10) * 7
d=((rut//10000)%10) * 6
e=((rut//1000)%10) * 5
f=((rut//100)%10) * 4
g=((rut//10)%10) * 3
h=((rut//1)%10) * 2
suma=(a+b+c+d+e+f+g+h)

resta1=(suma//11)
resta2=(suma-(resta1*11))
resta3=11-resta2

if (resta3 == 11):
    verificador="0"
elif (resta3 == 10):
    verificador="K"
else:
    verificador=str(resta3)

print("dv=", verificador)
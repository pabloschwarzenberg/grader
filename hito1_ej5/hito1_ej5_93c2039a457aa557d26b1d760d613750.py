#Cálculo del dígito verificador de un rut
rut=int(input("Ingrese el RUT(sin puntos): "))
verificador=""
a=(rut//10000000) * 3
b=((rut//1000000)%10) * 2
c=((rut//100000)%10) * 7
d=((rut//10000)%10) * 6
e=((rut//1000)%10) * 5
f=((rut//100)%10) * 4
g=((rut//10)%10) * 3
h=((rut//1)%10) * 2
suma=(a+b+c+d+e+f+g+h)

resto1=(suma//11)
resto2=(suma-(resto1*11))
resto_final=11-resto2
if (resto_final == 11):
    verificador="0"
elif (resto_final == 10):
    verificador="K"
else:
    verificador=str(resto_final)

print("dv=", verificador)
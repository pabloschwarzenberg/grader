#Cálculo del dígito verificador de un rut

rut = int(input("Ingrese su rut (sin punto, ni dígito verificador): "))

a=(rut%10) *2
b=((rut//10)%10) *3
c=((rut//100)%10) *4
d=((rut//1000)%10) *5
e=((rut//10000)%10) *6
f=((rut//100000)%10) *7
g=((rut//1000000)%10) *2
h=((rut//10000000)%10) *3

suma = (a+b+c+d+e+f+g+h)

div1 = (suma//11)

div2 = suma-(11*div1)

resul = 11 - div2

if resul == 11:
    print("dv=0")
elif resul == 10:
    print ("dv=K")
else:
    print("dv=",resul)
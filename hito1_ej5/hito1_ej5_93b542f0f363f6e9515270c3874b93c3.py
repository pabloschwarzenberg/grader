#Cálculo del dígito verificador de un rut
rut=input("INGRESE SU RUT: ")
rutstr=str(rut)
a=int(rutstr[0])*3
b=int(rutstr[1])*2
c=int(rutstr[2])*7
d=int(rutstr[3])*6
e=int(rutstr[4])*5
f=int(rutstr[5])*4
g=int(rutstr[6])*3
h=int(rutstr[7])*2
suma=a+b+c+d+e+f+g+h
pentera=int(suma/11)
resto=suma-(11*pentera)
total=11-resto
if total==11:
    dv=0
    print(dv)
elif total==10:
    dv="K"
    print(dv)
else:
    print(total)      
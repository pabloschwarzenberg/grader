#Cálculo del dígito verificador de un rut
rut = str(input("Ingrese un rut: "))

d8 = rut[7]
d7 = rut[6]
d6 = rut[5]
d5 = rut[4]
d4 = rut[3]
d3 = rut[2]
d2 = rut[1]
d1 = rut[0]

suma = int(d8)*2+int(d7)*3+int(d6)*4+int(d5)*5+int(d4)*6+int(d3)*7+int(d2)*2+int(d1)*3
modulo = suma//11
resto= suma-(11*modulo)
dv = 11-resto

if dv==11:
    print("dv=0")
elif dv==10:
    print("dv=K")
else:
    print(dv)
  
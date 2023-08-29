#Cálculo del dígito verificador de un rut
rut = int(input("Ingrese su Rut:"))
m = 2
suma = 0
while rut != 0:
    ultimo_digito = rut%10
    mp = ultimo_digito*m
    suma+=mp
    rut = rut//10
    m+=1
    if m==8:
        m = 2
resto = suma%11
dv = 11-resto
if dv==11:
    print("dv=",0)
elif dv==10:
    print("dv=k")
else:
    print("dv=",dv)

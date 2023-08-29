#Cálculo del dígito verificador de un rut
rut = str(input("INGRESE EL RUT SIN EL DIGITO VERIFICADOR: "))
rut = rut[::-1]
rut = list(rut)
n = 2
mult = 0
for i in rut:
    mult += int(i) * n
    if n == 7:
        n = 2
    else:
        n += 1
op = mult % 11
dv = ""
if 11 - op == 11:
    dv = "0"
elif 11 - op == 10:
    dv = "k"
else:
    dv = 11 - op
    
print("dv={0}".format(dv))

     
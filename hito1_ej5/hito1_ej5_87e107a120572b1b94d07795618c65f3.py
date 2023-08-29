#Cálculo del dígito verificador de un rut
constanteM = 2
suma = 0
rut = ""
rut2 = str(input("ingrese rut: "))
for j in rut2:
    rut = str (j) + rut
for i in rut:
    suma += int(i) * constanteM
    constanteM += 1 
    if constanteM == 8:
        constanteM = 2
division = suma//11
resto = suma - 11 * division
dv = 11 - resto
if (dv == 11):
    print("dv=0")
elif (dv == 10):
    print("dv=k")
else:
    print ("dv=", dv)
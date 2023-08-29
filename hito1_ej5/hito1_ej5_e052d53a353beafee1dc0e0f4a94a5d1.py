#Cálculo del dígito verificador de un rut
rut= input("Ingrese su numero de rut: ")
validacion =""
aux = 0
for i in range(len(rut)):
    rut_inv = rut[i]
    validacion = rut_inv + validacion
for a in range(len(rut)):
    calculo = int(validacion[a]) * ((a%6)+2)
    aux += calculo
   

div = aux%11
res = 11-div

if res == 11:
    print("dv = 0")
elif res == 10:
    print("dv = k")
else:
    print("dv = ", res)    
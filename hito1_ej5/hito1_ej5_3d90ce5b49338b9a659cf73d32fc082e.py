#Cálculo del dígito verificador de un rut
rut = int(input("Ingrese rut: "))

rut1 = list(str(rut))
rut2 = rut1[:]
monto = 0
dVer = 0
cont = 2
aux = len(rut1)
for i in range (aux):
    rut1[i], rut1[aux - i - 1] = rut2[aux - i - 1], rut2[i]
print(rut1)
for i in range(aux):
    monto = monto + ( int(rut1[i]) * cont)
    cont+=1
    if cont == 8:
        cont = 2
dVer = 11 - (monto % 11)
if dVer == 11:
    dVer = 0
if dVer == 10:
    dVer = "K"
print("dv=", dVer)
      
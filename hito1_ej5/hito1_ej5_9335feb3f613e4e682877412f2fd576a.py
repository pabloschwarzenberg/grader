numero = input("ingrese numero: ")
largo = len(numero)
m=1
sumador = 0
for x in range(largo-1,-1,-1):
    m = m + 1
    sumador = sumador + int(numero[x])*m
    if(m == 7):
        m = 1

resto = sumador%11

DV = 11 - resto

DV = str(DV)
if DV=="11":
    DV = "0"
if DV == "10":
    DV = "K"
print("dv=",DV)

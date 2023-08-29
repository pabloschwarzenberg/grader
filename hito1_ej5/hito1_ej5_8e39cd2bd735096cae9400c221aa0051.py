#Cálculo del dígito verificador de un rut
numero = input("ingrese el numero: ")
largo = len(numero)
print("\n")
i = 1
sumador = 0
for x in range(largo-1,-1,-1):
    i = i + 1
    sumador = sumador + int(numero[x]) *i
    if(i == 7):
        i = 1
resto = sumador%11
DV = 11 - resto
DV = str(DV)
if DV == "11":
    DV = "0"
if DV == "10":
    DV = "k"
print("dv=", DV)          
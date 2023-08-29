#Cálculo del dígito verificador de un rut
rut = int(input("ingrese un rut: "))
op = 0
for i in range(8):
    n = 2 + i
    if n > 7:
        n = i-4
    num = (rut // (10**(0+i))) % 10
    op += num*n
resto = op % 11
verificador = 11-resto
if verificador == 11:
    verificador = "0"
elif verificador == 10:
    verificador = "k"
else:
    verificador = str(verificador)
print("dv=",verificador)     
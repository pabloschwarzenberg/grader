#Cálculo del dígito verificador de un rut

#rut

rut = str(input("ingrese rut, sin punto , sin guión y digito verificador: "))
largo = len(rut)
rut = int(rut)
iterador = 0
factor = 0
suma = 0
while iterador <= largo:
    modulo = rut%10
    suma = suma + (modulo * factor)
    rut =//10
    iterador = iterador +1
    factor = factor + 1
    if factor ==8:
        factor= 2
resto = suma//11
DV = suma-(11*resto)
DV = 11 - DV
if DV ==11:
    print("dv=0")
if DV ==10:
    print("DV=k")
else:
    print("dv=",DV)
#Cálculo del dígito verificador de un rut
rut= str(input("Ingrese un RUT: "))
largo = len(rut)
rut = int(rut)
i = 0
factor = 2
suma = 0

while i <= largo:
    mod = rut%10
    suma = suma + (mod * factor)
    rut = rut // 10
    i += 1
    factor += 1
    if factor == 8:
        factor = 2
resto = suma // 11
DV = suma - (11 * resto)
DV = 11 - DV
if DV == 11:
    print("dv=0")
elif DV == 10:
    print("dv=k")
else:
    print("dv=", DV)     
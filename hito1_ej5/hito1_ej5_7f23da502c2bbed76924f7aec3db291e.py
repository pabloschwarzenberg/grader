#Cálculo del dígito verificador de un rut
rut = int(input("Ingrese un RUT sin dígito verificador: "))
suma = 0
multiplicador = 2
while rut > 0:
    suma += (rut % 10) * multiplicador
    rut //= 10
    multiplicador = 2 if multiplicador == 7 else multiplicador + 1
resto = suma % 11
if resto == 0:
    dv = '0'
elif resto == 1:
    dv = 'K'
else:
    dv = str(11 - resto)
print("dv=" + dv) 
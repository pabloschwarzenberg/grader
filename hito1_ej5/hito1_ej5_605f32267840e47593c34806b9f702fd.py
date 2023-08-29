#Cálculo del dígito verificador de un rut
rut = int(input("ingrese su rut sin puntos ni digito verificador: "))
rutStr = str(rut)
lista = list(rutStr)
cantidadN = len(lista)
suma = 0
multiplicador = 2
for a in range(cantidadN):
    digito = rut % 10
    rut = rut - digito
    rut = rut / 10
    multiplicacion = digito * multiplicador
    multiplicador = multiplicador + 1
    suma = suma + multiplicacion
    if multiplicador > 7:
        multiplicador = 2
division = suma // 11
formula = suma-(11*division)
resta = 11 - formula
dv = int(resta)
if dv == 10:
    dv = "k"
elif dv == 11:
    dv= 0
print("dv=", dv)
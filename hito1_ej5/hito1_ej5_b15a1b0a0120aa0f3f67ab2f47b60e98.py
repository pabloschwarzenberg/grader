#Cálculo del dígito verificador de un rut

#ENTRADA

rut = input("Ingrese su rut sin dv ")

#DESARROLLO

largo = len(rut)
multiplicadores = "234567"
suma = 0
dv = ""

#CICLO

contador = 0

while contador < largo:
    suma = suma + int(multiplicadores[contador % len(multiplicadores)]) * int(rut[-contador-1])
    contador += 1
dv = 11 - (suma % 11)

#SALIDAS

if dv == 10:
    print("dv=k")

elif dv == 11:
    print("dv=0")

else:
    print("dv=",+dv)     
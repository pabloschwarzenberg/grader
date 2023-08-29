#Cálculo del dígito verificador de un rut
num=int(input("Ingrese número: "))
num=str(num)
#dv=dígito verificador
serieNum = [2,3,4,5,6,7,2,3,4,5,6,7]
suma = 0
contador = 0
s = len(num)-1
for digitoSerie in serieNum:
    if contador < len(num):
        multiplicacion = int(num[s]) * digitoSerie
        suma = suma + multiplicacion
        s = s - 1
        contador = contador + 1

restoModulo = suma % 11
diferencia = 11 - restoModulo

if diferencia == 11:
    dv = 0
elif diferencia == 10:
    dv = "K"
else:
    dv = diferencia

print("dv=", dv)

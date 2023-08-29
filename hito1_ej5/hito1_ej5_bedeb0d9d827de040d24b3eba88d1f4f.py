#Cálculo del dígito verificador de un rut
numero = int(input("Ingrese numero: "))
numero = str(numero)

serieNum = [2, 3, 4, 5, 6, 7, 2, 3, 4, 5, 6, 7]

suma = 0
contador = 0
s = len(numero)-1
for digitoSerie in serieNum:
    if contador < len(numero):
        multiplicacion = int(numero[s]) * digitoSerie
        suma = suma + multiplicacion
        s = s - 1
        contador = contador + 1

restoModulo = suma % 11
resta = 11 - restoModulo

if resta == 11:
    digitoVerificador = 0
elif resta == 10:
    digitoVerificador = "K"
else:
    digitoVerificador = resta

print("dv=", digitoVerificador)
     
#Cálculo del dígito verificador de un rut
numb = int(input("numero: "))
numb = str(numb)
numeros = [2, 3, 4, 5, 6, 7, 2, 3, 4, 5, 6, 7]
sumar = 0
contador = 0
s = len(numb)-1
for digitoSerie in numeros:
    if contador < len(numb):
        multiplicacion = int(numb[s]) * digitoSerie
        sumar = sumar + multiplicacion
        s = s - 1
        contador = contador + 1
restoModulo = sumar % 11
restar = 11 - restoModulo
if restar == 11:
    digitoVerificador = 0
elif restar == 10:
    digitoVerificador = "K"
else:
    digitoVerificador = restar
print("dv=", digitoVerificador)
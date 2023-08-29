#Cálculo del dígito verificador de un rut
rut = input("Ingresa RUT sin digito verificador ni puntos: ")

cont = 0
suma = 0
out = ""


if len(rut) == 7:
	factor = "2345672"
else:
	factor = "23456723"


for i in range(len(rut)):
	aux = list(reversed(rut))
	a = aux[i]
	print(a)
	b = factor[i]

	suma = suma + ( int(a)*int(b) )

resto = suma%11
print(str(resto))

final = 11- resto

if final == 11:
	out = "0"
elif final == 10:
	out = "k"
else:
	out = str(final)


print("dv=" + out)

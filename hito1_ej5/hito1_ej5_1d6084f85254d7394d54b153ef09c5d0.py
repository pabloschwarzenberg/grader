#Cálculo del dígito verificador de un rut
rut = []
ingresar = [rut.append(numeros) for numeros in ("rut : >")]
rut.reverse()
recorrido = 2
multiplicar = 0

for x in rut:
    multiplicar+= int(x) * recorrido
if recorrido == 7: recorrido = 1
recorrido+= 1
modulo = multiplicar % 11
resultado = 11 - modulo
if resultado == 11: digito = 0
elif resultado == 10: digito = "k"
else: digito = resultado

print ("dv="+digito)
 
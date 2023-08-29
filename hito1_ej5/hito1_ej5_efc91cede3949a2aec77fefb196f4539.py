"""
7-. Escribe un programa que reciba como dato un número que representará un rut al que
debe calcularle el dígito verificador. Por ejemplo al ingresar 6016740 tu programa debiera
imprimir el siguiente mensaje:

dv=0

El algoritmo de cálculo del dígito verificador lo puedes obtener del siguiente link
"""

rut = input("RUT (sin digito verificador): ")

serie = [2, 3, 4, 5, 6, 7]
largo_serie = len(serie)
suma = 0
i = 0
for digito in rut[::-1]:
    digito = int(digito)
    valor_serie = serie[i]
    multiplicacion = digito*valor_serie
    suma += multiplicacion
    i += 1
    if i >= largo_serie:
        i = 0

division = int(suma/11)
resto = suma-(11*division)
resultado = 11-resto

if resultado == 11:
    dv = "0"
elif resultado == 10:
    dv = "K"
else:
    dv = str(resultado)

print("dv="+dv)


    
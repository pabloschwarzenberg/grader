rut = input("Ingrese rut:")
lista_rut = list(rut)
lista_rut.reverse()
index = 0
suma_mutiliplicacion = 0
serie = 2
while index < len(lista_rut):
    suma_mutiliplicacion += int(lista_rut[index]) * serie
    index += 1
    serie += 1
    if serie == 8:
        serie = 2
resultado = suma_mutiliplicacion % 11
digito_verificador = 11 - resultado
if digito_verificador == 11:
    print("dv=0")
elif digito_verificador == 10:
    print("dv=k")
else:
    print("dv=",digito_verificador)
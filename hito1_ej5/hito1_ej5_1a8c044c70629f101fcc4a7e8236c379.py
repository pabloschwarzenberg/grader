#Inicio
#Cálculo del dígito verificador de un rut
#Obtener el número del RUT sin el dígito verificador
rut = input("Ingrese el número del RUT (sin el dígito verificador): ")

#Calcular el dígito verificador
rut = rut[::-1]  #Invertir el RUT
factor = 2
suma = 0

for digito in rut:
    suma += int(digito) * factor
    factor += 1
    if factor > 7:
        factor = 2

dv = 11 - (suma % 11)
if dv == 11:
    dv = 0
elif dv == 10:
    dv = "K"

#Imprimir el dígito verificador
print("dv =", dv)
#Fin
      
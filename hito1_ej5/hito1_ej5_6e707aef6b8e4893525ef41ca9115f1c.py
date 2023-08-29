#Cálculo del dígito verificador de un rut
factor = 2
suma = 0
rut = input("Ingrese rut sin dígito verificador: ")
invertido = rut[::-1]
for digito in invertido:
    suma += int(digito) * factor
    factor += 1
    if factor == 8:
        factor = 2
dv = 11 - (suma % 11)
if dv == 11:
    dv = "K"
elif dv == 10:
    dv = "0"
completo = rut + "-" + str(dv)    
print(completo)
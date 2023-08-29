#Cálculo del dígito verificador de un rut
rut = input("Ingrese rut sin digito verificador: ")
rut_2 = ((rut)[::-1])

suma = 0
contador = 2
for numero in rut_2:
    numero = int(numero)
    multiplicacion = contador *numero
    suma += multiplicacion
    contador += 1
    if contador > 7:
        contador = 2
divicion = suma // 11
resto = suma - (11 * divicion)
resta = 11 - resto
if resta == 11:
    resta = 0
elif resta == 10:
    resta = "K"

print("dv = ",resta)




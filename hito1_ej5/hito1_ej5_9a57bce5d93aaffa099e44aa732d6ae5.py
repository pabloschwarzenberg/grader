#Cálculo del dígito verificador de un rut
rut=input('ingresar el rut(sin digito verificador): ')
#calcular el digito verificador 
suma=0
multiplicador= 2
for digito in reversed(rut):
    suma += int(digito) * multiplicador 
    multiplicador += 1
    if multiplicador == 8:
        multiplicador = 2
#calcular el resto
resto = suma % 11 
#determinar el digito verificador 
digito_verificador= 11-resto 
if digito_verificador == 11:
    digito_verificador = '0'
elif digito_verificador == 10:
    digito_verificador = 'k'
print('dv =', digito_verificador)
      
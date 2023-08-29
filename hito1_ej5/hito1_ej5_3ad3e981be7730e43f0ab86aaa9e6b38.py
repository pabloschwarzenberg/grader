rut = input("Ingrese un RUT sin dígito verificador: ")
rut = str(rut)  
rut = rut[::-1]  
factor = 2
suma = 0
for digito in rut:
    suma += int(digito) * factor
    factor += 1
    if factor == 8:
        factor = 2
        
digito_verificador = 11-(suma%11)
if digito_verificador == 11:
    print('dv = 0')
elif digito_verificador == 10:
    print('dv = K')
else:
    print("dv =", digito_verificador)
      
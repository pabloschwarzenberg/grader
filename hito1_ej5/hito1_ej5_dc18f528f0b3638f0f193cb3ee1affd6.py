#Cálculo del dígito verificador de un rut
rut = []
datos =[rut.append(numeros) for numeros in input ('RUT ::>')]
rut.reverse()
serie = 2
multiplicador = 0
for i in rut:
     multiplicador += (int(i)*serie)
     if serie == 7: serie = 1
     serie += 1
     modulo = multiplicador % 11
     resultado = 11 - modulo
     if resultado == 11: digito = 0
     elif resultado == 10: digito = "k"
     else: digito = resultado
print("dv=", digito)     
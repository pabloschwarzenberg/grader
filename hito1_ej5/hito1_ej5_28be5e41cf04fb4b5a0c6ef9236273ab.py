#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    rut =str(rut)
    rut =rut[::-1]
    multiplicador =2
    suma = 0
    for digito in rut:
        suma += int(digito ) *multiplicador
        multiplicador +=1
        if multiplicador >7:
           multiplicador =2
    digito_verificador = 11 -(suma % 11)
    if digito_verificador ==11:
        return '0'
    elif digito_verificador ==10:
        return 'k'
    else:
        return str(digito_verificador)
rut = input('ingrese el rut')
digito_verificador = calcular_digito_verificador(rut)
print('dv=',digito_verificador)
         

             
             
        
        
        
        
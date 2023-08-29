numero_a_verificar = input('Introduzca Numero:')
listado_multiplicador = [2,3,4,5,6,7,2,3,4,5,6,7,2,3,4,5,6,7,2,3,4,5,6,7,2,3,4,5,6,7,2,3,4,5,6,7,2,3,4,5,6,7,2,3,4,5,6,7,]
counter=0
resultado_temp = 0
for i in reversed(numero_a_verificar):
    multiplicador = listado_multiplicador[counter]
    resultado_temp += multiplicador*int(i)

    counter +=1
    

resultado_modulo11 = resultado_temp%11
digito_verificador = 11-resultado_modulo11
if resultado_modulo11 != 0 and resultado_modulo11 != 1:
    print('dv='+str(digito_verificador))
elif resultado_modulo11 == 0:
    print('dv=0')
elif resultado_modulo11 == 1:
    print('dv=k')

#30686957
        
#Nota final
print ('Ingrese sus notas sin coma. Ejemplo: 65 (seis coma cinco)')
PT = int(input('Nota PT: '))
PI = int(input('Nota PI: '))
NE = int(input('Nota NE: '))
PP = int(input('Nota PP: '))

promFinal = ((0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP))

print('Promedio final: '+str(promFinal))
#Suma de los N primeros números
print('\nSuma de los N primeros números\n')
try:
    
 n = int(input('Ingrese un número natural: '))
 if n > 0:
     
  output = n*(n+1)/2
  print ('La suma de los N primeros números naturales es: ',int(output))
 else:
     print('Sólo números naturales.')
     
except:
    print('Sólo números naturales.')

      
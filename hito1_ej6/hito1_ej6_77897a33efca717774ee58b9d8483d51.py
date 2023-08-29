#Ordenar tres números
numero1 = eval(input('Ingrese primer número'))
numero2 = eval(input('Ingrese segundo número'))
numero3 = eval(input('Ingrese tercer número'))

if numero1 <= numero2 <= numero3:
  print('El orden es: ',numero1,',',numero2,',',numero3,)
if numero1 <= numero3 <= numero2:
  print('El orden es: ',numero1,',',numero3,',',numero2,)
if numero2 <= numero1 <= numero3:
  print('El orden es: ',numero2,',',numero1,',',numero3,)
if numero2 <= numero3 <= numero1:
  print('El orden es: ',numero2,',',numero3,',',numero1,)
if numero3 <= numero1 <= numero2:
  print('El orden es: ',numero3,',',numero1,',',numero2,)
if numero3 <= numero2 <= numero1:
  print('El orden es: ',numero3,',',numero2,',',numero1,)
 
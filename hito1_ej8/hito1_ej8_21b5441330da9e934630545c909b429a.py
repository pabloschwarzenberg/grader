#Descomponer un número
numero = int(input('Ingresa un número de hasta 4 dígitos: '))

respaldo = numero

dU = numero%10
numero = numero//10

dD = numero%10
numero = numero//10

dC = numero%10
numero = numero//10

dM = numero

if 0 <= respaldo < 10:
  print(str(dU) + 'U')
    
if 10 <= respaldo < 100:
   print(str(dD) + 'D + ' + str(dU) + 'U')
    
if 100 <= respaldo < 1000:
    print(str(dC) + 'C + ' + str(dD) + 'D + ' + str(dU) + 'U')

if 1000 <= respaldo < 10000:
    print(str(dM) + 'M + ' + str(dC) + 'C + ' + str(dD) + 'D + ' + str(dU) + 'U')
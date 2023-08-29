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

    respuestaSinEspacios = str(dU) + 'U'
    
    print(dU, 'U')
    
if 10 <= respaldo < 100:

    respuestaSinEspacios = str(dD) + 'D + ' + str(dU) + 'U'
    
    print(dD, 'D + ', dU, 'U')
    
if 100 <= respaldo < 1000:

    respuestaSinEspacios = str(dC) + 'C + ' + str(dD) + 'D + ' + str(dU) + 'U'
     
    print(dC, 'C + ', dD, 'D + ', dU, 'U')
    
if 1000 <= respaldo < 10000:

    respuestaSinEspacios = str(dM) + 'M + ' + str(dC) + 'C + ' + str(dD) + 'D + ' + str(dU) + 'U'
        
    print(dM, 'M + ', dC, 'C + ', dD, 'D + ', dU, 'U')
  
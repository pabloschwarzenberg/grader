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

    respuesta = str(dU) + 'U'

    print(respuesta)
    
    
if 10 <= respaldo < 100:

    respuesta = str(dD) + 'D + ' + str(dU) + 'U'

    print(respuesta)
 
 
if 100 <= respaldo < 1000:

    respuesta = str(dC) + 'C + ' + str(dD) + 'D + ' + str(dU) + 'U'

    print(respuesta)
    
    
if 1000 <= respaldo < 10000:

    respuesta = str(dM) + 'M + ' + str(dC) + 'C + ' + str(dD) + 'D + ' + str(dU) + 'U'

    print(respuesta)
        
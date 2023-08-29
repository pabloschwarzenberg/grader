#Descomponer un número
numero = int(input('Ingresa un número de hasta 4 dígitos: '))
#numero = 1234

respaldo = numero

dU = numero%10          #numero%10 -> 1234%10 ->dU = 4
numero = numero//10     #numero//10 -> 1234//10 = 123 ->  numero = 123

dD = numero%10          #numero%10 -> 123%10 ->dD = 3
numero = numero//10     #numero//10 -> 123//10 = 12 ->  numero = 12

dC = numero%10          #numero%10 -> 12%10 ->dC = 2
numero = numero//10     #numero//10 -> 12//10 = 1 ->  numero = 1


dM = numero

if 0 <= respaldo < 10:

    respuestaSinEspacios = str(dU) + 'U'

    print(respuestaSinEspacios)
    
    print(dU, 'U')
    
if 10 <= respaldo < 100:

    respuestaSinEspacios = str(dD) + 'D + ' + str(dU) + 'U'

    print(respuestaSinEspacios)
    
    print(dD, 'D + ', dU, 'U')
    
if 100 <= respaldo < 1000:

    respuestaSinEspacios = str(dC) + 'C + ' + str(dD) + 'D + ' + str(dU) + 'U'

    print(respuestaSinEspacios)
    
    print(dC, 'C + ', dD, 'D + ', dU, 'U')
    
if 1000 <= respaldo < 10000:

    respuestaSinEspacios = str(dM) + 'M + ' + str(dC) + 'C + ' + str(dD) + 'D + ' + str(dU) + 'U'

    print(respuestaSinEspacios)
        
    print(dM, 'M + ', dC, 'C + ', dD, 'D + ', dU, 'U')      
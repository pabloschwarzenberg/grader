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
    se = str(dU) + 'U'
    print(se)        
if 10 <= respaldo < 100:    
    se = str(dD) + 'D + ' + str(dU) + 'U'    
    print(se)    
if 100 <= respaldo < 1000:
    se = str(dC) + 'C + ' + str(dD) + 'D + ' + str(dU) + 'U'
    print(se)        
if 1000 <= respaldo < 10000:
    se = str(dM) + 'M + ' + str(dC) + 'C + ' + str(dD) + 'D + ' + str(dU) + 'U'
    print(se)
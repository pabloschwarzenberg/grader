#Descomponer un número
numero = int(input('Ingrese un numero de hasta 4 dígitos: '))

respaldo = numero

dU = numero%10                                                  
numero = numero//10                                             

dD = numero%10                                                   
numero = numero//10                                             

dC = numero%10                                                  
numero = numero//10                                             

dM = numero

if 0<= respaldo <=9:                                            
    respuestaSinEspacios = str(dU) + 'U'
    print(respuestaSinEspacios)                                
    
if 10 <= respaldo <= 99:                                        
    print(dD,'D +',dU,'U')                                     
    
if 100 <= respaldo <= 999:                                      
    print(dC,'C +',dD,'D +',dU,'U')                             
    
if 1000 <= respaldo <= 9999:                                 
    print(dM,'M +',dC,'C +',dD,'D +',dU,'U')  
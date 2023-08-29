#Cálculo del dígito verificador de un rut
rut = str(input("ingrese el numero de rut: "))                                  
while  len(rut)<7:                                                                  
   rut = str(input("Error, ingrese el numero de rut: "))                        
contador =len(rut)                                                                  
acumulador = 0                                                                      
x=0                                                                                 
y=2                                                                                 
verificador=0                                                                       
while contador != 0:                                                                
    acumulador = acumulador + (int(rut[x]) * y)                                     
    x=x+1                                                                           
    y=y+1                                                                           
    contador=contador - 1                                                           
    if y == 8:                                                                      
       y=2                                                                          
y=acumulador /11                                                                    
t=acumulador-(11*y)                                                                 
verifica = acumulador % 11                                                          
verificador= 11-verifica                                                            
print ("dv= ", verificador)                                   
                                                                                    
                                                                                    
                                                                                    
                                                                                    
                                                                                    
                                                                                          
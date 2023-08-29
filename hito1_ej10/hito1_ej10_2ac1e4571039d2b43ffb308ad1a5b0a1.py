from time import sleep                                                      
saldocajero = 1000000                                                       
saldousuario = 100000                                                       
user = str(int(input("Ingrese el usuario: ")))                              
passw = str(int(input("Ingrese la contraseña: ")))                          
while True:                                                                 
    if user == "10334151" and passw == "1803":                              
        print("Usuario y contraseña correctos")                             
        sleep(1)                                                            
        monto_a_retirar = int(input("Ingrese el monto a retirar: "))        
        if monto_a_retirar>saldousuario and monto_a_retirar>saldocajero:    
            print("monto no permitido")                                     
            break                                                           
        if monto_a_retirar<saldousuario and monto_a_retirar<saldocajero:    
            saldo_usuario_final = saldousuario-monto_a_retirar              
            saldo_cajero_final = saldocajero-monto_a_retirar                
            print("saldo cuenta=", saldo_usuario_final)                     
            print("saldo cajero=", saldo_cajero_final)                      
        if monto_a_retirar!="N":                                            
            break                                                           
    if user != "10334151" or passw != "1803":                               
        print("clave invalida")                                             
        sleep(1)                                                            
        print("INTENTO N°2")                                                
        sleep(1)                                                            
        passw = str(int(input("Ingrese la contraseña denuevo: ")))          
        if user != "10334151" or passw != "1803":                           
            print("clave invalida")                                         
            sleep(1)                                                        
            print("INTENTO N°3")                                            
            sleep(1)                                                        
            passw = str(int(input("Ingrese la contraseña denuevo: ")))      
            if user != "10334151" or passw != "1803":                       
                print("tarjeta bloqueada")                                  
                break                                                       
      
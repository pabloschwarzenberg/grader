#Cajero Automático

saldo_cajero = 1000000
saldo_usuario = 100000
a = str(int(input("Usuario: ")))
b = str(int(input("Contraseña: ")))
while True:

    if a == "10334151" and b == "1803":
        print("El Usuario y la Contraseña correctos")
        
        monto_a_retirar = int(input("Monto a retirar: "))
        
        if monto_a_retirar>saldo_usuario and monto_a_retirar>saldo_cajero:
            
            print("monto no permitido")
            
            break
        
        if monto_a_retirar<saldo_usuario and monto_a_retirar<saldo_cajero:
            
            saldo_usuario_final = saldo_usuario-monto_a_retirar
            
            saldo_cajero_final = saldo_cajero-monto_a_retirar
            
            print("saldo cuenta=", saldo_usuario_final)
            
            print("saldo cajero=", saldo_cajero_final)
        
        if monto_a_retirar!="N":
            
            break
    
    if a != "10334151" or b != "1803":
        
        print("contraseña invalida")
        
        print("INTENTO N°2")
        
        b = str(int(input("Ingrese nuevamente la contraseña: ")))
        
        if a != "10334151" or b != "1803":
            
            print("contraseña invalida")
            
            print("INTENTO N°3")
            
            contrasena = str(int(input("Ingrese nuevamente la contraseña: ")))
            
            if a != "10334151" or b != "1803":
                
                print("tarjeta bloqueada")
                
                break
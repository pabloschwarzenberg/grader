#Cajero Automático
saldo_cajero = 1000000
saldo_usuario = 100000
a = str(int(input("Usuario: ")))
b = str(int(input("Contraseña: ")))
while True:

    if a == "10334151" and b == "1803":
        
        print("El Usuario y la Contraseña son correctos")
        
        monto_a_retirar = int(input("Ingrese el monto a retirar: "))
        
        if monto_a_retirar>saldo_usuario and monto_a_retirar>saldo_cajero:
            
            print("monto no permitido")
            
            break
        
        if monto_a_retirar<saldo_usuario and monto_a_retirar<saldo_cajero:
            
            saldo_usuario_final = saldo_usuario-monto_a_retirar
           
            saldo_cajero_final = saldo_cajero-monto_a_retirar
            
            print("saldo cuenta=", saldo_usuario_final)
            
            print("saldo cajero=", saldo_cajero_final)
            
            b20k = int(monto_a_retirar/20000)
            monto_a_retirar = monto_a_retirar%20000
            b10k = int(monto_a_retirar/10000)
            monto_a_retirar = monto_a_retirar%10000
            b5k = int(monto_a_retirar/5000)
            monto_a_retirar = monto_a_retirar%5000
            
            print("billetes 20000= ", b20k)
            print("billetes 10000= ", b10k)
            print("billetes 5000= ", b5k)
        
        if monto_a_retirar!="C":
            
            break      
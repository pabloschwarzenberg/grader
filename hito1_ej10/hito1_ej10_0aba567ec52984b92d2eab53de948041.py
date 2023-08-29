#Cajero Automático
saldo_delcajero = 1000000
saldo_delusuario = 100000
usuario = str(int(input("Coloque el usuario: ")))
contrasena = str(int(input("Coloque la contraseña: ")))

while True:
    if usuario == "10334151" and contrasena == "1803":
        print("Usuario y contraseña correctos")
        
        monto_a_retirar = int(input("Coloque el monto a retirar: "))
        if monto_a_retirar>saldo_delusuario and monto_a_retirar>saldo_delcajero:
            print("monto invalido")
            break
        if monto_a_retirar<saldo_delusuario and monto_a_retirar<saldo_delcajero:
            saldo_usuario_final = saldo_delusuario-monto_a_retirar
            saldo_cajero_final = saldo_delcajero-monto_a_retirar
            print("saldo de cuenta=", saldo_usuario_final)
            print("saldo del cajero=", saldo_cajero_final)
        if monto_a_retirar!="N":
            break
    if usuario != "10334151" or contrasena != "1803":
        print("clave erronea")
        
        print("INTENTO N°2")
        
        contrasena = str(int(input("Coloque la contraseña denuevo: ")))
        if usuario != "10334151" or contrasena != "1803":
            print("clave erronea")
            
            print("INTENTO N°3")
            
            contrasena = str(int(input("Coloque la contraseña denuevo: ")))
            if usuario != "10334151" or contrasena != "1803":
                print("tarjeta bloqueada momentaneamente")
                break
#Cajero Automático
cajero = 1000000
usuario_registrado = "10334151"
clave_registrada = "1803"
cuenta = 100000
intento = 0

while intento <= 3 :
    usuario = input("Por favor, ingrese su usuario: ")
    clave = input("Por favor, ingrese su contraseña: ")
    
    if usuario == usuario_registrado and clave == clave_registrada:
        print("Usuario aceptado, bienvenido al sistema")
        intento = 4
        while True:
                    retiro = eval(input("¿Cuanto monto desea retirar: "))
                    if retiro > cuenta:
                         print("Monto no permitido")
                    
                        
    
                    else:
                        cuenta2 = cuenta - retiro
                        cajero2 = cajero-retiro
                        cajero = cajero2
                        cuenta = cuenta2
                        print("saldo cuenta = ", cuenta)
                        print("Saldo cajero = ", cajero)
                        opcion = input("Si desea salir, escriba algo distinto de N: ")
                        if opcion != "N":
                            break
                        
                    
                        
                
    else:
        intento = intento+1
        print("Usuario y/o contraseña, incorrecta")
        if intento == 3:
            print("Tarjeta bloqueada")
            break      
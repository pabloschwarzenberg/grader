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
                    retiro = eval(input("Cuanto monto desea retirar: "))
                    if retiro > cuenta:
                         print("Monto no permitido")
                         continue
                         
                    b2 = retiro//20000
                    if b2 > 0 :
                        r2 = retiro - (b2*20000)
                        print("billetes 20000=", b2)
                    else:
                        r2 = retiro
                        
                    b1 = r2//10000
                    if b1 > 0:
                        r3 = r2 -(b1*10000)
                        print("billetes 10000=", b1)
                    else:
                        r3 = r2
                    b5 = r3//5000
                    
                    if b5 > 0:
                        r4 = r3-(b5*5000)
                        print("billetes 5000=", b5)
                    else:
                        r4 = r3
                        
                    b4 = r4//1000
                    
                    if b4 > 0:
                        print("billetes 1000=", b4)

                        
                     
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
 
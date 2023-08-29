#Cajero Automático
saldo_cajero= 1000000
saldo_usuario= 100000
intentos= 0
sacar= "si"
monto= 0
salir ="no"
while salir == "no": 
    intentos= 0
    sacar= "si"
    monto= 0
    salir ="no"
    print ("BIENVENIDO AL BANCO DE LA PLAZA")
    print (" ")
    while intentos < 3 and sacar=="si":
        usuario= str(input("Ingrese su nombre de usuario: "))
        clave= str(input("Ingrese la clave: "))
        if usuario== "10334151" and clave== "1803":
            while sacar== "si":
                monto= int(input("Ingrese monto del dinero a retirar: "))
                if monto > saldo_usuario:
                    print("Monto no permitido.")
                    monto== 0 and sacar== "si"
                else:
                    saldo_usuario= saldo_usuario - monto
                    saldo_cajero= saldo_cajero - monto
                    print("Saldo actual de la cuenta: ",saldo_usuario)
                    print("Saldo actual del cajero: ",saldo_cajero)
                    if saldo_usuario == 0:
                        sacar="no"
                        print("------------------------------------------------------")
                        print ("AGOTÓ SU DE DINERO, GRACIAS POR OPERAR CON NOSOTROS")
                        print("------------------------------------------------------")
                    else:
                        sacar= input("¿Desea sacar más dinero? (si/no): ")
        else:
            intentos= intentos + 1
            print("Clave o usuario incorrecto.")
            print("Le quedan ", 3 - intentos, "intento(s)")
    if intentos == 3:
        print("Tarjeta bloqueada.")
        print (" ")
    else:    
        print (" ")
    # salir= input("¿Desea salir de programa? (si/no)")
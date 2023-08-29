#Cajero Automático
 
saldocaj = 1000000
funca = 1
usuario1 = 10334151
contrasenna1 = 1803
saldousuario = 100000
logscr = 1
attempt = 0
while funca == 1:
    if logscr == 1:
        logid = int(input('Ingresar numero de usuario: '))
        logpass = int(input('Ingrese clave: '))
        if (logid == usuario1) and (logpass == contrasenna1):
            logscr = 2
        else:
            attempt += 1
            print ("clave invalida")
            if attempt >= 3:
                print ("tarjeta bloqueada")
                funca = 0
    if logscr == 2:
        giro = int(input("Monto a retirar: "))
        if (giro > saldousuario) or (giro > saldocaj):
            print('monto no permitido')
        else:
            saldousuario -= giro
            saldocaj -= giro
            print('saldo cuenta=', saldousuario)
            print('saldo cajero=', saldocaj)
            opc = input('presione N para volver a girar, para salir del programa, cualquier otra tecla: ')
            if (opc == "N"):
                logscr = 2
            else:
                funca = 0
else:
    print("fin")
      
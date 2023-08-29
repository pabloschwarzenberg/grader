#Cajero Automático
usuario = int(input("Ingrese el usuario: "))
clave = int(input("Ingrese su clave: "))

intentos = 1
saldo_cajero = 1000000
saldo_usuario = 100000
user = 10334151
cont = 1803

while clave != cont:
    intentos += 1

    if intentos > 3:
        break
    print("La clave ingresada no es correcta.")
while clave == cont:
        print("La clave ingresada es correcta.")
        print("Su saldo es",saldo_usuario)
        giro = int(input("Ingrese saldo a retirar: "))
        if giro <= saldo_usuario:
            saldo_usuario = saldo_usuario-giro
            saldo_cajero = saldo_cajero-giro
            print("Saldo de cuenta es=",saldo_usuario,",","Saldo cajero=",saldo_cajero)
        elif giro > saldo_usuario:
            giro=int(input("El saldo ingresado exede el maximo, intentelo de nuevo:"))
            if giro <= saldo_usuario:
                saldo_usuario = saldo_usuario - giro
                print("Su nuevo saldo es:", saldo_usuario)
            elif giro > saldo_usuario:
                print("Su sesion se ha cerrado, intente nuevamente")
        break      
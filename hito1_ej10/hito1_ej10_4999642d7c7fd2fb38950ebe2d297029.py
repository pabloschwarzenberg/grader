#Cajero Automático
usuario = int(input("Ingrese el usuario: "))
clave = int(input("Ingrese su clave: "))

intentos = 1
saldo_cajero = 1000000
saldo_usuario = 100000
user = 10334151
cont = 1803

billetes_20 = 20000
billetes_10 = 10000
billetes_5 = 5000

while clave != cont:
    intentos += 1

    if intentos > 3:
        break
    print("clave invalida")
while clave == cont:
        print("clave correcta")
        print("su saldo es",saldo_usuario)
        giro = int(input("ingrese saldo a retirar: "))
        if giro <= saldo_usuario:
            saldo_usuario = saldo_usuario-giro
            saldo_cajero = saldo_cajero-giro
            print("saldo cuenta=",saldo_usuario,",","saldo cajero=",saldo_cajero)
        elif giro > saldo_usuario:
            giro=int(input("exede el maximo intentelo de nuevo:"))
            if giro <= saldo_usuario:
                saldo_usuario = saldo_usuario - giro
                print("su nuevo saldo es:", saldo_usuario)
            elif giro > saldo_usuario:
                print("cesion cerrada intentelo de nuevo")
        break
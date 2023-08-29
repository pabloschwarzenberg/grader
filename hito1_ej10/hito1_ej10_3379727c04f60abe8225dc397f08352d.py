#Cajero Automático
usuario = "10334151"
clave = "1803"
intentos = 3
Termino = False
saldo = 1000000
saldoUsuario = 100000
while intentos > 0:
    cliente = input("Ingrese el usuario")
    password = input("Ingrese la clave: ")
    if cliente == usuario and password == clave:
        solicitud = True
    else:
        solicitud = False

    if solicitud == True:
        while Termino == False:
            monto = int(input("Cuanto dinero desea retirar: "))
            saldoActualizado = saldo - monto
            saldoUsuarioActualizado = saldoUsuario - monto
            saldos = []
            if saldoActualizado > 0 and saldoUsuarioActualizado > 0:
                saldo = saldoActualizado
                saldoUsuario = saldoUsuarioActualizado
            else:
                print("monto no permitido")
            a = ("saldo cuenta={}".format(saldoUsuario))
            b = ("saldo cajero={}".format(saldo))
            print(a)
            print(b)
            print("\nSi desea continuar coloque N si desea salir coloque cualquier otra tecla")
            opcion = input()
            if opcion == "N":
                Termino = False
            else:
                Termino = True
        intentos = -1
    else:
        print("Clave o usuario equivocado\n")
        intentos -= 1
    if intentos == 0:
        print("tarjeta bloqueada")
        break    
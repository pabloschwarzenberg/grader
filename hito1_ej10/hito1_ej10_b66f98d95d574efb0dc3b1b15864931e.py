#Cajero Automáticousuario = "10334151"
usuario = "10334151"
clave = "1803"
intentos = 3
Termino = False
saldo = 1000000
saldo_usuario = 100000
while intentos > 0:
    user = input("ingrese el usuario")
    password = input("ingrese la clave: ")
    if user == usuario and password == clave:
        solicitud = True
    else:
        solicitud = False

    if solicitud == True:
        while Termino == False:
            monto = int(input("Cuanto dinero desea retirar: "))
            saldo_actualizado = saldo - monto
            saldo_usuario_actualizado = saldo_usuario - monto
            saldos = []
            if saldo_actualizado > 0 and saldo_usuario_actualizado > 0:
                saldo = saldo_actualizado
                saldo_usuario = saldo_usuario_actualizado
            else:
                print("monto no permitido")
            a = ("saldo cuenta={}".format(saldo_usuario))
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

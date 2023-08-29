#Cajero Automático
Usuario = "10334151"
Clave = "1803"
Intentos = 3
Termino = False
Saldo = 1000000
Saldo_Usuario = 100000
while Intentos > 0:
    Cliente=input("ingrese un usuario: ")
    Password=input("Ingrese la clave: ")
    if Cliente==Usuario and Password==Clave:
        Solicitud=True
    else:
        Solicitud=False
    if Solicitud==True:
        while Termino == False:
            Monto=int(input("Cuanto dinero desea retirar: "))
            Saldo_Actua=Saldo-Monto
            Saldo_Usuario_Actua=Saldo_Usuario-Monto
            Saldos = []
            if Saldo_Actua> 0 and Saldo_Usuario_Actua > 0:
                Saldo = Saldo_Actua
                Saldo_Usuario = Saldo_Usuario_Actua
            else:
                print("monto no permitido")
            a = ("saldo cuenta={}".format(Saldo_Usuario))
            b = ("saldo cajero={}".format(Saldo))
            print(a)
            print(b)
            print("\nSi desea continuar coloque N si desea salir coloque cualquier otra tecla")
            Opcion=input()
            if Opcion=="N":
                Termino=False
            else:
                Termino=True
        intentos=-1
    else:
        print("Clave o usuario equivocado\n")
        Intentos -= 1
    if Intentos == 0:
        print("tarjeta bloqueada")
        break    
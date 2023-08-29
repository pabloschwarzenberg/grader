#Cajero Automático
Cuenta = 10334151
Clave = 1803
SaldoCajero = 1000000
SaldoUsuario = 100000
Contador = 0
Funcionamiento = True
Retiro = 0

while Funcionamiento:
    
    CuentaIngresada = int(input("Ingrese su numero de cuenta"))
    while CuentaIngresada != Cuenta:
        CuentaIngresada  = int(input("Ingrese su numero de cuenta"))

    while Contador != 3:
        ClaveIngresada = int(input("Ingrese su clave"))
        Contador = Contador+1
        if ClaveIngresada == 1803:
            break
        else:
            print("Clave invalida")

        
    if Contador == 3:
        Funcionamiento = False
        print ("Tarjeta Bloqueada")
        break

    Retiro = int(input("Ingrese su monto a retirar"))
    while Retiro > SaldoUsuario:
        print("Monto no permitido")
        Retiro = int(input("Ingresa nuevamente el retiro"))

    SaldoUsuario = SaldoUsuario - Retiro
    SaldoCajero = SaldoCajero - Retiro

    print ("Saldo cuenta=",SaldoUsuario)
    print ("Saldo cajero=",SaldoCajero)

    Salir = str(input("Si desea continuar presione n"))
    if Salir != "n":
        Funcionamiento = False

    Contador = 0
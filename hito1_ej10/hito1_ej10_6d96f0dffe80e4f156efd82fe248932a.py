#Cajero Automático
ClaveUsuario = int(input("Ingrese su clave: "))
SaldoInicial = 1000000
SaldoCuenta = 100000

i = 1
while ClaveUsuario != 1803 and i < 3:
    ClaveUsuario = int(input("Clave invalida: "))
    i = i + 1
    if ClaveUsuario != 1803 and i == 3:
        print("Tarjeta Bloqueada")
i = 3
RetiroUsuario = int(input("Ingrese el monto que desea retirar: "))
while ClaveUsuario == 1803 and SaldoCuenta >= RetiroUsuario and i == 3:
    if RetiroUsuario <= SaldoCuenta:
        SaldoCuenta = SaldoCuenta - RetiroUsuario
        print("Saldo cuenta =", SaldoCuenta)

        SaldoInicial = SaldoInicial - RetiroUsuario
        print("Saldo cajero =", SaldoInicial)

    else:
        print("Monto no permitido")      
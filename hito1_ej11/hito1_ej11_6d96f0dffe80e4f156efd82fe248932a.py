#Cajero Automático
ClaveUsuario = int(input("Ingrese su clave: "))
SaldoCajero = 1000000
SaldoCuenta = 100000
Billetede20 = 20
Billetede10 = 40
Billetede5 = 40

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

        SaldoCajero = SaldoCajero - RetiroUsuario
        print("Saldo cajero =", SaldoCajero)

    if RetiroUsuario % 20000 == 0:
        Billetede20 = RetiroUsuario // 20000
        R = RetiroUsuario % 20000
        Billetede10 = (R % 20000) // 10000
        Billetede5 = (R % 20000) // 5000
        print("Billetes 20000 =" + str(Billetede20))
        print("Billetes 10000 =" + str(Billetede10))
        print("Billetes 5000 =" + str(Billetede5))

    else:
        Billetede20 = RetiroUsuario // 20000
        R = RetiroUsuario % 20000
        if R % 10000 == 0:
            Billetede10 = R // 10000
            Billetede5 = (R % 10000) // 5000
            print("Billetes 20000 =" + str(Billetede20))
            print("Billetes 10000 =" + str(Billetede10))
            print("Billetes 5000 =" + str(Billetede5))

        else:
            Billetede10 = R // 10000
            R = R % 10000
            Billetede5 = R // 5000
            print("Billetes 20000 =" + str(Billetede20))
            print("Billetes 10000 =" + str(Billetede10))
            print("Billetes 5000 =" + str(Billetede5))

else:
    print("Monto no permitido")      
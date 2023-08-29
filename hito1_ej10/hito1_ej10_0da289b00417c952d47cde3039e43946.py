#Cajero automatico lvl 1
usuario = int(input("Ingrese numero de usuario: "))
clave = int(input("Ingrese clave: "))
saldo_cajero = 1000000
saldo_cuenta = 100000
if clave != 1803:
        cont = 0
        while clave != 1803 and cont < 2:
            clave = int(input("Clave invalida, reingrese clave: "))
            cont = cont + 1

if clave == 1803:
    while usuario == 10334151 and clave == 1803:
        monto = int(input("Ingrese monto a retirar: "))
        while monto > 100000 or saldo_cuenta < 0:
            monto = int(input("Ingrese monto valido: "))

        clave2 = int(input("Verifique su clave: "))
        if clave2 != clave:
            cont = 0
            while clave2 != 1803 and cont < 2:
                clave = int(input("Clave invalida, reingrese clave: "))
                cont = cont + 1
        if clave == 1803 and saldo_cuenta > 0 and saldo_cajero > 0:
            saldo_cajero = saldo_cajero - monto
            saldo_cuenta = saldo_cuenta - monto
            print("Saldo cuenta= " , saldo_cuenta)
            print("Saldo cajero= " , saldo_cajero)
            x = input("¿Desea retirar mas dinero?(N = Si)(Any key = NO): ")
            if x != "N":
                break
            else:
                continue
        elif saldo_cuenta == 0:
                print("No puede retirar mas dinero")
                break
    print("Vuelva pronto :)")
#Cajero Automático
usuario = '10334151'
clave = '1803'
saldo_cajero = 1000000
usu = input("Ingrese su usuario: ")
cla = input("Ingrese su clave: ")

if usu == usuario and cla == clave:
    n = 0
    cla = ''
    while cla != clave and n < 3:
        cla = input("Ingrese su clave nuevamente: ")
        if cla != clave:
            print("clave invalida")
        n += 1
        if n == 3:
            print("Tarjeta bloqueada")
        if cla == clave:
            saldo_cuenta = 100000
            dinero_retirado = 0
            salir = True
            while saldo_cuenta > 0 and salir:
                dinero_retirado = int(input("Indique un monto para retirar: $"))
                if dinero_retirado > 100000:
                    print("monto invalido")
                else:
                    saldo_cuenta = saldo_cuenta - dinero_retirado
                    saldo_cajero = saldo_cajero - dinero_retirado
                    print("\nSaldo cuenta = $",saldo_cuenta,"\nSaldo cajero = $",saldo_cajero)
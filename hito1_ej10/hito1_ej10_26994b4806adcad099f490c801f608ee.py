i = 0
saldo = 1000000
cuenta = 100000
saldof = 0
usuario=10334151
contra=1803
retiro=45000
while i <= 3:
    if usuario == 10334151:
        if contra == 1803:
            if 0 < retiro <= 100000:
                cuenta = cuenta - retiro
                saldo = saldo - retiro
                print("saldo cuenta=", cuenta)
                print("saldo cajero=", saldo)
                i = 4
            else:
                print("Monto no permitido")
        else:
            print("Clave invalida")
            i = i + 1
        if i == 3:
            print("Tarjeta bloqueada.")
            break
    else:
        print("Usuario incorrecto.")
      
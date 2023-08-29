#Cajero Automático
while 1 == 1:
    usuario = int(input("Usuario:"))
    clave = int(input("Clave:"))
    if usuario == 10334151 and clave == 1803:
        monto = int(input("monto a retirar:"))
        if monto >= 100000:
            print("monto no permitido")
        else:
            print("saldo cuenta=", 100000 - monto)
            print("saldo cajero=", 1000000 - monto)
        break

    if usuario != 10334151 or clave != 1803:
        monto = int(input("Ingrese el monto a retirar:"))
        print("clave invalida")
        i += 1
        if i == 3:
            print("tarjeta bloqueada")
            break

      
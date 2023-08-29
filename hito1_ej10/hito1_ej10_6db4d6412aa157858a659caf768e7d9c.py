usuario = input("Usuario: ")
saldo_en_cajero = 1000000
saldo_disponible = 100000
retirar = 0
ver = True
con = 0
i = 0
while ver:
    clave = input("Clave: ")
    if clave != "1803":
        print("Clave Inválida")
        con += 1
        if con == 3:
            print("Tarjeta Bloqueada")
            ver = False
            break
    elif clave == "1803":
        while ver:
            retirar = input("Ingrese Monto a Retirar: ")
            if retirar == "N":
                continue
            elif retirar == "Y":
                ver = False
                break
            elif int(retirar) > saldo_disponible:
                print("Monto no permitido")
            else:
                saldo_disponible -= int(retirar)
                saldo_en_cajero -= int(retirar)
                print("Saldo cuenta=", saldo_disponible)
                print("Saldo cajero=", saldo_en_cajero)
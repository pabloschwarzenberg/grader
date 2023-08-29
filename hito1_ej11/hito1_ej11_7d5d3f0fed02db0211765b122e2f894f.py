#Cajero Automático
usuario = input("Usuario: ")
saldo_en_cajero = 1000000
saldo_disponible = 100000
retirar = 0
ver = True
con = 0
i = 0
b20k = 0
b10k = 0
b5k = 0
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
                retirar = int(retirar)
                saldo_disponible -= retirar
                saldo_en_cajero -= retirar
                while retirar >= 20000:
                    b20k = retirar // 20000
                    retirar -= b20k * 20000
                while retirar >= 10000:
                    b10k = retirar // 10000
                    retirar -= b10k * 10000
                while retirar >= 5000:
                    b5k = retirar // 5000
                    retirar -= b5k * 5000
                    if retirar < 5000 and retirar != 0:
                        saldo_disponible += retirar
                        print("El monto sobrante ha sido reincorporado a la cuenta.")

                
                print("Saldo cuenta=", saldo_disponible)
                print("Saldo cajero=", saldo_en_cajero)
                print("Billetes 20000=", b20k)
                print("Billetes 10000=", b10k)
                print("Billetes 5000=", b5k) 
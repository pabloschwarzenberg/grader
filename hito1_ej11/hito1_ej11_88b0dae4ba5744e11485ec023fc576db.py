#Cajero Automático
usuario = str(input("Usuario: "))
contraseña = str(input("Contraseña: "))
intento = 0
plataU = 100000
plataC = 1000000
lista = [20000, 10000, 5000]

if usuario == "10334151":
    if contraseña == "1803":
        while True:
            retirar = input("Monto a retirar: ")
            cont = 0
            for i in retirar:
                if i != "N":
                    cont = 0
                else:
                    cont += 1
            if cont == 0 and len(retirar) == 1:
                break

            while int(retirar) < 1 or int(retirar) > 100000:
                print("Monto no valido")
                retirar = input("Monto a retirar: ")
            plataU -= int(retirar)
            plataC -= int(retirar)
            print("saldo cuenta={}".format(plataU))
            print("saldo cajero={}".format(plataC))
            for i in lista:
                if int(retirar) % i == 0:
                    cantidad = int(int(retirar) / i)
                    billetes = str(i)
            print("billetes {}={}".format(billetes, cantidad))
    else:
        while contraseña != "1803":
            print("clave invalida")
            intento += 1
            if intento == 3:
                print("tarjeta bloqueada")
                break
            contraseña = input("Contraseña: ")



      
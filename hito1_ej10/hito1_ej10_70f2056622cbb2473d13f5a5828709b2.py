#Cajero Automático
def validar():
    cont = 0
    while True:
        usuario = 10334151
        clave = 1803
        if usuario != 10334151 and clave != 1803:
            cont += 1
            if cont == 3:
                print("tarjeta bloqueada")
                break
            print("clave invalida")
        else:
            banco()
            break


def banco():
    while True:
        cajero = 1000000
        cuenta = 100000
        retirar = 45000
        if retirar > cuenta or retirar < 0:
            print("monto no permitido")
            break

        else:
            cajero = cajero - retirar
            cuenta = cuenta - retirar
            print("saldo cuenta=", cuenta)
            print("saldo cajero=", cajero)
            break

validar()
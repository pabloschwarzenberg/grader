#Cajero Automático
trys = 0
play = True
u = int(input("Ingrse Usuario: "))
while play:
    trys += 1
    if trys <= 3:
        c = int(input("Ingrese Clave: "))
        if c == 1803:
            m = int(input("Ingrese monto a retirar: "))
            if m > 100000:
                print("monto no permitido")
            elif m < 100000:
                sc = 100000 - m
                sca = 1000000 - m
                print("saldo cuenta=",sc)
                print("saldo cajero=",sca)
            play = False
        elif c != 1803:
            print("clave invalida")
    else:
        print("tarjeta bloqueada")
        play = False
        break
     
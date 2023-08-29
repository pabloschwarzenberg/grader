#Cajero Automático
saldo = 1000000
clave = 1803
saldou = 100000
i = 0
while True:
    usuario = eval(input("Ingrese usuario: "))
    if usuario == 10334151:
        while True:
            claveu = eval(input("Ingrese la clave: "))
            if claveu != clave:
                i +=1
                if i == 3:
                    print("tarjeta bloqueada")
                    break
                else:
                    print("clave invalida")
                    continue
            else:
                while True:
                    monto = eval(input("Ingrese monto: "))
                    if monto > saldou:
                        print("monto no permitido")
                    else:
                        saldou = saldou-monto
                        saldo = saldo-monto
                        print("saldo cuenta =",saldou,"\n saldo cajero =",saldo)
                        break
            break
    else:
        print("usuario no válido")
    break
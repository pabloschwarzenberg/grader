#Cajero Automático
datos = {"usuario" : "10334151", "clave" : "1803"}#diccionario usuario

saldocu = [100000]
saldoca = [1000000]
#while de ingreso
intentos = 0
while intentos < 3:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")
    if clave != datos["clave"] and usuario != datos["usuario"]:
        print("clave invalida")
        intentos += 1
        if intentos == 3:
            print("tarjeta bloqueada")
            exit()

    elif clave == datos["clave"] and usuario == datos["usuario"]:
        i = 1
        while i != 0:
            montor = int(input("Ingrese el monto a retirar: "))
            if montor < 100000 and montor > 100000:
                print("monto no permitido")
                i = 1
            else:
                p1 = 0
                p2 = 0
                saldoinicial = saldocu[p1] - montor
                saldocajero = saldoca[p2] - montor
                saldocu.append(saldoinicial)
                saldoca.append(saldocajero)
                p1 += 1
                p2 += 1
                print("saldo cuenta={}".format(saldoinicial))
                print("saldo cajero={}".format(saldocajero))
                i = 0

    seguir = str.upper(input("Si quiere salir ingrese cualqiuer letra distinta de N: "))
    if seguir == "N":
            intentos = 0
    elif seguir != "N":
            intentos = 4

#Cajero Automático
saldoc = 1000000
saldou = 100000
acceso = False
retirado = False

user = int(input("Ingrese su usuario: "))
if user == 10334151 :
    for x in range(3):
        pw = int(input("Ingrese su contraseña: "))
        if pw == 1803 :
            acceso = True
            break
        elif x == 2:
            print("Maximo de intentos alcanzados, tarjeta bloqueada")
            break
        else:
            print("Intento",x+1,"Fallido, intente otra vez")
    if acceso == True :
        print("Acceso autorizado")
        while retirado == False :
            monto =  int(input("Ingrese el monto a retirar: "))
            if monto <= 100000 :
                saldoc -= monto
                saldou -= monto
                print("saldo cuenta="+str(saldou))
                print("saldo cajero="+str(saldoc))
                retirado = True
            else:
                print("Monto no permitido")
                retirado = False
else:
    print("Usuario sin cuenta bancaria")

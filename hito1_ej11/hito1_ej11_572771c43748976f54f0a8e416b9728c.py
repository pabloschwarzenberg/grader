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
                b20  = int(monto/20000)
                print("billetes 20000="+str(b20))
                saldnv = monto-(b20*20000)
                b10 = int(saldnv/10000)
                print("billetes 10000="+str(b10))
                saldnvv  = saldnv-(b10*10000)
                b5 = int(saldnvv/5000)
                print("billetes 5000="+str(b5))
                
                retirado = True
            else:
                print("Monto no permitido")
                retirado = False
else:
    print("Usuario sin cuenta bancaria")

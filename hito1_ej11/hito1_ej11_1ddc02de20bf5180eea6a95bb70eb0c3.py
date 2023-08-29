#Cajero Automático
usuario=int(input("Ingresa tu Usuario:"))
while usuario!=10334151:
    int(input("Error, Ingresa tu Usuario:"))
clave=int(input("Ingresa tu clave:"))
intentos=0
saldocuenta=100000
saldocajero=1000000
bi20mil=20
bi10mil=40
bi5mil=40
while not(clave==1803):
    intentos=intentos+1
    if intentos==3:
        print("¡Tarjeta bloqueada!")
        break
    else:
        clave=int(input("Ingrese su clave:"))

if intentos!=3:
    respuesta="S"
    while(respuesta=="S"):
        montoretirado=int(input("Ingresa el monto a retirar:"))        
        if montoretirado<=saldocuenta:
            if montoretirado<=saldocajero:
                saldocuenta=saldocuenta-montoretirado
                saldocajero=saldocajero-montoretirado
                retira20mil=0
                retira10mil=0
                retira5mil=0
                while(montoretirado>0):
                    if montoretirado>=20000 and bi20mil>0:
                        retira20mil=retira20mil+1
                        bi20mil=bi20mil-1
                        montoretirado=montoretirado-20000

                    if montoretirado>=10000 and bi10mil>0:
                        retira10mil=retira10mil+1
                        bi10mil=bi10mil-1
                        montoretirado=montoretirado-10000

                    if montoretirado>=5000 and bi5mil>0:
                        retira5mil=retira5mil+1
                        bi5mil=bi5mil-1
                        montoretirado=montoretirado-5000
                
                print("saldo cuenta=",saldocuenta)
                print("saldo cajero=",saldocajero)
                print("billetes 20000=",retira20mil)
                print("billetes 10000=",retira10mil)
                print("billetes 5000=",retira5mil)
        else:
            print("Monto no permitido")                     
        respuesta=input("Desea realizar otro retiro? (S/N):")      
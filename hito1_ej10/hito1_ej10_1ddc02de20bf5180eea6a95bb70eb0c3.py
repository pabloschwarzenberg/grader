#Cajero Automático
usuario=int(input("Ingresa tu Usuario:"))
while usuario!=10334151:
    int(input("Error, Ingresa tu Usuario:"))
clave=int(input("Ingresa tu clave:"))
intentos=0
saldocuenta=100000
saldocajero=1000000

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
                print("saldo cuenta=",saldocuenta)
                print("saldo cajero=",saldocajero)
        else:
            print("Monto no permitido")                     
        respuesta=input("Desea realizar otro retiro? (S/N):")       
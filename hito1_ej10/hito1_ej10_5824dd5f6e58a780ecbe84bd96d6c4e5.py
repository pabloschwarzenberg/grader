#Cajero Automático
intentos = 3
clave = 1803
r =10334151

while(intentos  != 0):
    saldocajero =1000000
    rut = int(input("Ingrese rut: "))
    cl = int(input("Ingrese clave: "))
    if(cl == clave and r == rut):
        saldocuenta = 100000
        retira = int(input("Indique el monto a retirar:"))
        if retira <saldocajero:
            saldocajero = saldocajero - retira
            saldocuenta = saldocuenta - retira
            print("Saldo Cuenta: {}".format(saldocuenta))
            print("Saldo cajero: {}".format(saldocajero))
        else:
            print("Monto no permitido")

    else:
        intentos -= 1
        print("Le quedan {} intentos".format(intentos))

if(intentos == 0):
    print("Tarjeta Bloqueada")
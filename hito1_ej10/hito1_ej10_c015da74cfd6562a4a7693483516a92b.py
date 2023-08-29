#Cajero Automático
saldocuenta=100000
saldocajero=1000000

usuario=10334151
clave=1803

error=0

USUARIO=int(input("Ingrese usuario:"))
CLAVE=int(input("Ingrese clave:"))


while CLAVE!=clave:
    print("clave invalida")
    CLAVE=int(input("Ingrese clave nuevamente:"))
    error+=1
    if error==3:
        print("tarjeta bloqueada")
        break



if USUARIO==usuario and CLAVE==clave:
    retiro=int(input("Cuanto va a retirar?"))
    while retiro>saldocuenta:
        print("monto no permitido")
        retiro=int(input("Cuanto va a retirar?"))
        
        
    saldocuenta=saldocuenta-retiro
    saldocajero=saldocajero-retiro

print("saldo cuenta=",saldocuenta)
print("saldo cajero=",saldocajero)


      
#Cajero Automático
saldoc=100000
saldoca=1000000
cuenta=10334151
clave=1803
clave1=0
intentos=3
cantidad=0
opcion="N"
cuenta=int(input("Ingresa la cuenta: "))
while intentos!=0:
    clave1=int(input("Ingresa la clave: "))
    if clave1!=clave:
               intentos=intentos-1
               print("Clave invalida")
    elif clave1==clave:
        break

while saldoc!=0 and opcion=="N" and clave1==clave:
    cantidad=int(input("Cuanto quieres retirar: "))
    opcion=input("si quieres salir escribe algo diferente a (N): ")
    if cantidad>100000:
        print("monto invalido")
        saldoc=saldoc
        saldoca=saldoca
        print("Saldo de la cuenta: ",saldoc)
        print("Saldo del cajero: ",saldoca)
    elif cantidad<100000:
        saldoc=saldoc-cantidad
        saldoca=saldoca-cantidad
        print("Saldo de la cuenta: ",saldoc)
        print("Saldo del cajero: ",saldoca)

if intentos==0:
    print("tarjeta bloqueada")
elif opcion!="N":
    print("Gracias por el cajero")     
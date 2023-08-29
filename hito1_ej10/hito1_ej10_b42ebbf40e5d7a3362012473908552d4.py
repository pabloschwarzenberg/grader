#Cajero Automático
usuario=int(input("ingrese su usuario:"))
clave=int(input("ingrese su clave:"))
monto=int(input("ingrese monto a retirar:"))
saldocajero=1000000-monto
saldocuenta=100000-monto
if (clave==1803)and(monto<=100000):
    print("saldo cuenta=",saldocuenta)
    print("saldo cajero=",saldocajero)
elif (clave==1803)and(monto>100000):
    print("monto no permitido")
elif (clave!=1803):
    print("clave inválida")
    dos=int(input("ingrese clave:"))
elif (dos==1803)and(monto<=100000):
    print("saldo cuenta=",saldocuenta)
    print("saldo cajero=",saldocajero)
elif (dos==1803)and(monto>100000):
    print("monto no permitido")
elif (dos!=1803):
    print("clave inválida")
    tres=int(input("ingrese clave:"))
elif (tres==1803)and(monto<=100000):
    print("saldo cuenta=",saldocuenta)
    print("saldo cajero=",saldocajero)
elif (tres==1803)and(monto>100000):
    print("monto no permitido")
else:
    print("tarjeta bloqueada")      
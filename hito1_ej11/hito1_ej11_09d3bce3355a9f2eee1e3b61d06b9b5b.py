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
if (monto==(5000)or(15000)or(25000)or(35000)or(45000)or(55000)or(65000)or(75000)or(85000)or(95000)):
    print("billetes 5000=",round(monto/5000))
elif(monto==(10000)or(30000)or(50000)or(70000)):
    print("billetes 10000=",round(monto/10000))
elif(monto==(20000)or(40000)or(60000)or(80000)or(100000)):
    print("billetes 20000=",round(monto/20000))
else:
    print("monto no válido")
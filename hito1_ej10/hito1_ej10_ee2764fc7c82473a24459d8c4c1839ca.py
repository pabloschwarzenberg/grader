#Cajero Automático
usuario=int(input("ingrese su usuario:"))
clave=int(input("ingrese su clave:"))
saldo_cajero=1000000
saldo_cuenta=100000
intentos=0
while clave!= 1803:
    print("clave invalida")
    if intentos==3:
        print("tarjeta bloqueada")
        break;
if clave==1803:
    monto=input("¿Monto a retirar?:")
    monto=int(monto)
    if monto>100000:
        print("Monto no permitido")
    else:
        saldo_cuenta= saldo_cuenta-monto
        saldo_cajero= saldo_cajero-monto
print("saldo cuenta=",saldo_cuenta)
print("saldo cajero=",saldo_cajero)
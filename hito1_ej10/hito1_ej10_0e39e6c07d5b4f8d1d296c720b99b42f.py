#Cajero Automático
# Cajero Automático
usuario = int(input("usuario: "))
clave = int(input("clave: "))
saldo_inicial=1000000
saldo_cajero =int()
saldo_cuenta=int()
saldo=100000
#print(saldo_inicial)
if clave!=1803:
 i= 1
 while i<3:
    print("clave invalida")
    clave = int(input("clave: "))
    i+=1
    if i ==3:
     print("tarjeta bloqueada")

if clave==1803:
    saldo==100000
    print("saldo=100000")
    monto=int(input("monto a retirar: "))
    if 0 < monto <= 100000:
        print("monto permitido")
        saldo_cuenta=saldo-monto
        saldo_cajero =saldo_inicial- monto
        print("saldo cuenta=",saldo_cuenta)
        print("saldo cajero=",saldo_cajero)
    else:
        print("monto no permitido")

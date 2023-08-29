#Cajero Automático
saldo_cajero= 1000000
saldo_cuenta= 100000
usuario=0
while usuario!=10334151:
    usuario = int(input("Ingrese su numero de usuario: "))
    if usuario!=10334151:
        print("ingrese un usuario válido")

i=0
while i != 3:
    clave = int(input("Ingrese su clave: "))
    if clave==1803:
        break
    else:
        print("clave invalida")
    i=i+1
    if i==3:
        print("Tarjeta Bloqueada")
retiro=int(input("Ingrese el monto a retirar: "))
if retiro>saldo_cuenta:
    print("monto no permitido")
if retiro<=saldo_cuenta:
    print("saldo cuenta="+str(saldo_cuenta-retiro))
    print("saldo cajero="+str(saldo_cajero-retiro))
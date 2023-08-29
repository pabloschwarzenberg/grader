si=1000000
sc=100000
tries=1
b20=0
b10=0
b5=0
usu=int(input("Ingrese usuario: "))
while usu!=10334151:
    print("Usuario no válido")
    usu=int(input("Ingrese usuario: "))
clave=int(input("Ingrese su clave: "))
while clave!=1803 and tries!=3:
    print("Clave inválida")
    tries=tries+1
    clave=int(input("Ingrese su clave: "))
if tries==3:
    print("Tarjeta bloqueada")
    exit()
else:
    tries=1

monto=int(input("Ingrese monto a retirar: "))
while monto<=0 or monto>100000:
    print("Monto no permitido")
    monto=int(input("Ingrese monto a retirar: "))

si= si-monto
sc= sc-monto

if (monto-20000)>=0:
    while monto>19999:
        monto=monto-20000
        b20=b20+1
if (monto-10000)>=0:
    while monto>9999:
        monto=monto-10000
        b10=b10+1
if (monto-5000)>=0:
    while monto>4999:
        monto=monto-5000
        b5=b5+1

print("Saldo cuenta=",sc)
print("Saldo cajero=",si)
print("Billetes 20000=",b20)
print("Billetes 10000=",b10)
print("Billetes 5000=",b5)
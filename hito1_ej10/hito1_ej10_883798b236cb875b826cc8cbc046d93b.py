#Cajero Automático
si=1000000
sc=100000
tries=1
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

print("Saldo cuenta=",sc)
print("Saldo cajero=",si)
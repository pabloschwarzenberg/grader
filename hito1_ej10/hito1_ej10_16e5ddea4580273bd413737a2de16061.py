import sys
usuario = int(input("Usuario : "))
pw = int(input("Contraseña : "))
saldocajero = 1000000
saldocuenta = 100000
contador=0
while pw!=1803 and usuario!=10334151:
    contador+=1
    print("Usuario o clave invalida")
    print("Reingrese los datos ")
    usuario = int(input("Usuario : "))
    pw = int(input("Contraseña : "))
    if contador==3:
        print("tarjeta bloqueada")
        sys.exit()
        
monto = int(input("Monto a retirar : "))
while monto>saldocuenta:
    print("monto no permitido")
    monto = int(input("Reingrese el monto a retirar\n==> "))

saldocuenta-=monto
saldocajero-=monto

print("Saldo cuenta=", saldocuenta)
print("Saldo cajero=", saldocajero)

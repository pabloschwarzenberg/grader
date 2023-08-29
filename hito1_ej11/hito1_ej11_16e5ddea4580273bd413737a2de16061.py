import sys
usuario = int(input("Usuario : "))
pw = int(input("Contraseña : "))
saldocajero = 1000000
saldocuenta = 100000
contador=0
while pw!=1803:
    contador+=1
    print("clave invalida")
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

print("saldo cuenta=", saldocuenta)
print("saldo cajero=", saldocajero)
billete_20=monto//20000
billete_10=(monto-billete_20*20000)//10000
billete_5=(monto-(billete_20*20000+billete_10*10000))//5000
print("billetes 20000=",billete_20)
print("billetes 10000=",billete_10)
print("billetes 5000=",billete_5)
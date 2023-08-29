#Cajero Automático
import sys
usuario=input("Ingrese el numero de usuario:")
clave=int(input("Ingrese la clave:"))


contraseña=1803
saldo_cuenta=100000
saldo_cajero=1000000

cant_bill_20mil=20
cant_bill_10mil=40
cant_bill_5mil=40


cont=0

while clave!=contraseña:
    if cont==2:
        print("Tarjeta bloqueada")
        sys.exit()
    
    print("Clave Invalida")
    clave=int(input("Ingrese nuevamente la clave:"))
    cont=cont+1


monto_re=int(input("Ingrese el monto que desea retirar:"))

while monto_re<=0 or monto_re>saldo_cuenta:
    print("Monto invalido")
    monto_re=int(input("Ingrese nuevamente el monto a retirar:"))

saldo_cuenta_final=saldo_cuenta-monto_re
saldo_cajero_final=saldo_cajero-monto_re

bill_20000=monto_re//20000

print("saldo cuenta=",saldo_cuenta_final)
print("saldo cajero=",saldo_cajero_final)

print("billetes 20000=",bill_20000)

s=input("Ingrese una letra distinta de N para salir :")
while s=="N":
    print("Letra invalida")
    s=input("Ingrese una letra distinta de N para salir :")

#Cajero Automático
Usuario=int(input("ingrese su usuario"))
clave=int(input("ingrese su clave"))
saldocajero = 1000000
Clave=0

while clave!=1803 and Clave<3:
    Clave+=1
    print("clave invalida")
    clave=int(input("ingrese nuevamente"))
    while Clave==3:
        print("tarjeta bloqueada")
                
            
saldocuenta = 100000
retirar=int(input("que monto desea retirar"))
saldofinal=saldocuenta-retirar
saldocajerof=saldocajero-retirar
if saldocuenta<retirar:
    print("monto no permitido")
else:
    print("el saldo cuenta = ", saldofinal)
    print("el saldo cajero =", saldocajerof)
    terminar=input("presione una letra diferente de N para terminar")
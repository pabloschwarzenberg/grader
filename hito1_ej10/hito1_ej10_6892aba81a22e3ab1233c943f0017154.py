#Cajero Automático
Saldoi = 1000000
Saldoic = 100000
u = int(input("Ingresar usuario : "))
while u != 10334151:
    u = int(input("Error, Ingrese usuario: "))
i = 0
c = int(input("Ingresar clave : "))
while c != 1803:
    c = int(input("clave invalida: "))
    i= i+1
    if i == 2:
        print("tarjeta bloqueada")
        break

if i !=2:
    MontoS = int(input("Monto a retirar: "))
    while MontoS>Saldoic:
        MontoS= int(input("monto no permitido: "))
        a =Saldoi-MontoS
        b =Saldoic-MontoS
        print("saldo cuenta=", a)
        print("saldo cajero=", b)
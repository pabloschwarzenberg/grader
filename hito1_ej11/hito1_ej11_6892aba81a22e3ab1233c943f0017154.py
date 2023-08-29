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
    sobrante1= Saldoi-MontoS
    sobrante2= Saldoic-MontoS
    print("saldo cuenta="+str(sobrante2))
    print("saldo cajero="+str(sobrante1))
    for moneda in[20000,10000,5000]:
        cantidadMon= MontoS//moneda
        sobrante= MontoS%moneda
        if cantidadMon!=0:
            print("billetes"+str(moneda)+"="+str(cantidadMon))
        MontoS=sobrante  
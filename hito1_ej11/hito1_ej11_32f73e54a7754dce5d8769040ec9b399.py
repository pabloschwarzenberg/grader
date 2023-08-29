usuario = int(input("ingrese su usuario:"))
clave = int(input("ingrese su clave:"))
monto = int(input("ingrese monto a retirar:"))

billetes1 = 20000
billetes2 = 10000
billetes3 = 5000

totalBilletes20 = billetes1 * 20
totalBilletes10 = billetes2 * 40
totalBilletes5 = billetes3 * 40

billetesImpresos20 = monto // billetes1
montoRestante1 = monto - billetesImpresos20

billetesImpresos10 = montoRestante1 // billetes2
montoRestante2 = montoRestante1 - billetesImpresos10

billetesImpresos5 = montoRestante2 // billetes3

saldocajero= totalBilletes20 + totalBilletes10 + totalBilletes5 - monto
saldocuenta=100000-monto



if (clave == 1803) and (monto <= 100000):
    print("saldo cuenta=", saldocuenta)
    print("saldo cajero=", saldocajero)
    print("billetes 20000=", billetesImpresos20)
    print("billetes 10000=", billetesImpresos10)
    print("billetes 5000=", billetesImpresos5)
elif (clave == 1803) and (monto > 100000):
    print("monto no permitido")
elif (clave != 1803):
    print("clave inválida")
    dos = int(input("ingrese clave:"))
elif (dos == 1803) and (monto <= 100000):
    print("saldo cuenta=", saldocuenta)
    print("saldo cajero=", saldocajero)
    print("billetes 20000=", billetesImpresos20)
    print("billetes 10000=", billetesImpresos10)
    print("billetes 5000=", billetesImpresos5)
elif (dos == 1803) and (monto > 100000):
    print("monto no permitido")
elif (dos != 1803):
    print("clave inválida")
    tres = int(input("ingrese clave:"))
elif (tres == 1803) and (monto <= 100000):
    print("saldo cuenta=",saldocuenta)
    print("saldo cajero=",saldocajero)
    print("billetes 20000=", billetesImpresos20)
    print("billetes 10000=", billetesImpresos10)
    print("billetes 5000=", billetesImpresos5)
elif (tres == 1803) and (monto > 100000):
    print("monto no permitido")
else:
    print("tarjeta bloqueada")


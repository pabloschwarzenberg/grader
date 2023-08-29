#Cajero Automático
usuario = int(input("Ingrese su usuario: "))
saldoC = 1000000
saldoU = 100000
bD = 20
bV = 40
bC = 40
i = 0
b = -2
while i<3:
    clave = int(input("Ingrese su clave: "))
    if clave == 1803:
        montoR = int(input("Cuanto dinero desea retirar: "))
        if montoR>100000:
            print("monto no permitido")
            i = 5
        else:
            c = montoR%10000
            d = (montoR//10000)*1000
            d1 = (montoR//10000)
            saldoU = saldoU - montoR
            saldoC = saldoC - montoR
            print("saldo cuenta="+str(saldoU))
            print("saldo cajero="+str(saldoC))
            k = montoR-d
            ki = k // 20000
            print("billetes 20000="+str(ki))
            if d1%2 != 0:
                print("billetes 10000=1")
            if c == 5000:
                print("billetes 5000=1")
            i = 5
    if clave != 1803:
        b+=1
        if b==1:
            print("tarjeta bloqueada")
            i+=1
        if b!=1:
            print("clave inválida")
            i+=1
     

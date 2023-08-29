#Cajero Automático
usuario = int(input("Ingrese su usuario: "))
saldoC = 1000000
saldoU = 100000
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
            saldoU = saldoU - montoR
            saldoC = saldoC - montoR
            print("saldo cuenta="+str(saldoU))
            print("saldo cajero="+str(saldoC))
            i = 5
    if clave != 1803:
        b+=1
        if b==1:
            print("tarjeta bloqueada")
            i+=1
        if b!=1:
            print("clave inválida")
            i+=1
     
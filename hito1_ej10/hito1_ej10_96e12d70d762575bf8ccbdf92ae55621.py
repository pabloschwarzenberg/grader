#Cajero Automático

usua=int(input("ingrese un usuario: "))
clave=int(input("ingrese una clave: "))

intento=1
saldocaj=1000000
saldocuen=100000

if clave != 1803 and usua == 10334151:
    while clave!=1803:
        print("clave invalida")
        print("llevas ",intento," intento de 3")
        usua=int(input("ingrese un usuario: "))
        clave=int(input("ingrese una clave: "))
        intento=intento+1
        print("llevas ",intento," intento de 3")
if clave!=1803 and intento==3:
        print("tarjeta bloqueada")
        

if clave==1803 and usua==10334151 and intento<3:
    montoret=int(input("monto a retirar: "))
    if montoret>100000:
        while montoret>100000:
            print("monto no permitido")
            montoret=int(input("monto a retirar: "))
    if montoret<=100000:
        print("saldo cuenta=",saldocuen-montoret)
        print("saldo cajero=",saldocaj-montoret)

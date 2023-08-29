#Cajero Automático

usua=int(input("ingrese un usuario: "))
clave=int(input("ingrese una clave: "))

intento=1
saldocaj=1000000
saldocuen=100000

bill20=20000
bill10=10000
bill5=5000

def billetes_resto(a, b):
    billetes = a // b
    resto = a % b
    return billetes, resto

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
        saldocuen -= montoret
        saldocaj -= montoret
        a, r = billetes_resto(montoret, bill20)
        b, r = billetes_resto(r, bill10)
        c, r = billetes_resto(r, bill5)
        
        print("saldo cuenta=" + str(saldocuen))
        print("saldo cajero=" + str(saldocaj))
        print("billetes 20000=" + str(a))
        print("billetes 10000=" + str(b))
        print("billetes 5000=" + str(c))
#Cajero Automático
a = int(input("Usuario :"))
saldo=1000000
caja=100000
intento=1
if a == 10334151:
    while True:
        if intento<=3:
            b = int(input("Clave :"))
            if b == 1803:
                c = int(input("monto a retirar :"))
                if c >=0 and c<=caja:
                     saldo=saldo-c
                     caja=caja-c
                     print("saldo cuenta=",caja)
                     print("saldo cajero=",saldo)
                     break
                else:
                    print("monto no permitido")
                    break
            if intento<3:
                print("error")
                intento=intento+1
            elif intento==3:
                print("tarjeta bloqueada")
                break
        else:
            print("tarjeta bloqueada")
            break
else:
    print("error usuario")

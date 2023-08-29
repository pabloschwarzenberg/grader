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
                     if c > 20000:
                         c1 = c//20000
                         print("billetes 20000=",c1)
                         c = c-(c1*20000)
                         if c > 10000:
                             c2 = c // 10000
                             print("billetes 10000=",c2)
                             c = c-(c2*10000)
                             if c > 5000:
                                c3 = c // 5000
                                print("billetes 5000=",c3)
                                c = c-(c3*5000)
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

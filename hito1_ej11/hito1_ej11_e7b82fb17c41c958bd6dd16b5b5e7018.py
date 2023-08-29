#cajero automatico
usuario=int(input("ingrese usuario: "))
while(usuario!=10334151):
      usuario=int(input("ERROR; ingrese nuevamente el usuario: "))

clave=int(input("ingrese clave: "))
intento=0
while not(clave!=1083):
    intento=intento+1

    if intento==3:
        print("TARJETA BLOQUEADA")
        break
    else:
        clave=int(input("ingrese clave: "))
if intento!=3:
    montocajero=1000000
    montousuario=100000
    bill20=20
    bill10=40
    bill5=40
    monto=int(input("ingrese monto a retirar: "))
    while (monto>=montocajero and monto<=montocajero):
        monto=int(input("ingrese un monto acorde a su saldo: "))
    montousuario=montousuario-monto
    montocajero=montocajero-monto
    retira20mil=0
    retira10mil=0
    retira5mil=0
    while (monto>0):
        if monto>=20000 and bill20>0:
            retira20mil=retira20mil+1
            bill20=bill20-1
            monto=monto-20000

        if monto>=10000 and bill10>0:
            retira10mil=retira10mil+1
            bill10=bill10-1
            monto=monto-10000

        if monto>=5000 and bill5>0:
            retira5mil=retira5mil+1
            bill5=bill5-1
            monto=monto-5000
    print("saldo cuenta=",montousuario)
    print("saldo cajero=",montocajero)
    print("billetes 20000=",retira20mil)
    print("billetes 10000=",retira10mil)
    print("billetes 5000=",retira5mil)
    
    
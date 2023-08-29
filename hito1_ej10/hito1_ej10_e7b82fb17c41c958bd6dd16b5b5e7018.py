#Cajero Automático


usuario=int(input("ingrese usuario: "))
while(usuario!=10334151):
      usuario=int(input("ERROR; ingrese nuevamente el usuario: "))

clave=int(input("ingrese clave: "))
intento=0
while not (clave!=1083):
    intento=intento+1

    if intento==3:
        print("TARJETA BLOQUEADA")
        break
    else:
        clave=int(input("ingrese clave: "))
if intento!=3:
    montocajero=1000000
    montousuario=100000
    monto=int(input("ingrese monto a retirar: "))
    while (monto>1000000 and monto<=0):
        monto=int(input("ingrese un monto acorde a su saldo: "))
    saldo=montousuario-monto
    saldocajero=montocajero-monto
    print("saldo cuenta=",saldo)
    print("saldo cajero=",saldocajero)
    

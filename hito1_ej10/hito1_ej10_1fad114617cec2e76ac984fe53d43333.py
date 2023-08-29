usuario=int(input("usuario"))
clave=int(input("clave"))
saldocajero=1000000
ensucuenta=100000
contador=0
while contador<4:
    if clave==1803:
        monto=int(input("monto a retirar"))
        if monto<=ensucuenta and monto<=saldocajero:
            ensucuenta=ensucuenta-monto
            saldocajero=saldocajero-monto
            print("saldo cuenta="+str(ensucuenta)+"  "+"saldo cajero="+str(saldocajero))
            contador=8
        else:
            print("monto no permitido")
    elif clave!=1803:
        contador=contador+1
        print("clave invalida")
if 3<contador<7 :
    print("tarjeta bloqueada")
    
      
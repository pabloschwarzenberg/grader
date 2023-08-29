#Cajero Automático
usuario_valido=10334151
monto_cuenta=100000
saldo_cajero=1000000
clave_valida=1803
billetes_20=20
billetes_10=40
billetes_5=40
cont=0
def cant_billetes(x):
    cant_20=int(x/20000)
    restante=x-(cant_20*20000)
    print("billetes 20000=",cant_20,sep="")
    if restante!=0:
        cant_10=int(restante/10000)
        restante2=restante-(cant_10*10000)
        print("billetes 10000=",cant_10,sep="")
    elif restante2!=0:
        cant_5=int(restante2/5000)
        restante3=restante2-(cant_5*5000)
        print("billetes 5000=",cant_5,sep="")
    return
while True:
    if cont==3:
        break
    usuario=input(10334151)
    if usuario!=usuario_valido:
        break
    while usuario==usuario_valido:
        if monto_cuenta!=100000:
            break
        clave=int(input("1803"))
        if clave!=clave_valida:
            cont+=1
            print("clave invalida")
            if cont==3:
                print("tarjeta bloqueada")
                break
        while clave==clave_valida:
            monto_retiro=int(input("35000"))
            if not (monto_retiro<=monto_cuenta and monto_retiro>=0 and (monto_retiro%5000)==0):
                print("monto no permitido")
            elif (monto_retiro<=monto_cuenta and monto_retiro>=0 and (monto_retiro%5000)==0):
                monto_cuenta=monto_cuenta-monto_retiro
                print("saldo cuenta=",monto_cuenta,sep="")
                print("saldo cajero=",saldo_cajero-monto_retiro,sep="")
                print(cant_billetes(monto_retiro))
                break

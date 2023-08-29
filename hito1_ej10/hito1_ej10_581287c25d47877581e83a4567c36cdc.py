#Cajero Automático
usuario_valido=10334151
monto_cuenta=100000
saldo_cajero=1000000
clave_valida=1803
cont=0
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
            monto_retiro=int(input("45000"))
            if not (monto_retiro<=monto_cuenta and monto_retiro>=0):
                print("monto no permitido")
            elif (monto_retiro<=monto_cuenta and monto_retiro>=0):
                monto_cuenta=monto_cuenta-monto_retiro
                print("saldo cuenta=",monto_cuenta,sep="")
                print("saldo cajero=",saldo_cajero-monto_retiro,sep="")
                break
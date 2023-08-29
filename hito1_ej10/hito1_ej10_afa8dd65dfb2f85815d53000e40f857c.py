#Cajero Automático
n=True
while n:
    intentos=3
    while intentos>0:
        usuario=int(input("ingrese usuario:"))
        clave=int(input("ingrese clave:"))

        if (usuario==10334151) and (clave==1803):
            print('Bienvenido' )
            break
        else:
            print('clave invalida')
            intentos=intentos-1
    if (intentos==0):
        print('tarjeta bloqueada')
    else:
        saldo_inicial= 1000000
        saldo_cuenta= 100000
        monto=int(input("ingrese monto:"))
        
        if (saldo_cuenta<monto):
            print('monto no permitido')

        elif (saldo_cuenta>=monto):
            saldo_cajero=saldo_inicial-monto
            saldo_final_cuenta=saldo_cuenta-monto
            print("saldo cuenta=",saldo_final_cuenta)
            print("saldo cajero=",saldo_cajero)
            print('Hasta luego')
            n=False
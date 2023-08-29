#Cajero Automático
intentos=3
saldo_cajero=1000000
saldo_cuenta=100000
while(intentos>0):

    usuario=input("ingrese usuario: ")
    clave=input("ingrese clave secreta: ")

    if(usuario=='10334151') and (clave=='1803'):
        print("acceso concedido")
        ingrese_saldo=int(input("ingrese monto: "))
        if saldo_cuenta>=ingrese_saldo:
            saldo_cajero=saldo_cajero-ingrese_saldo
            saldo_cuenta=saldo_cuenta-ingrese_saldo
            print("espere")
            print("saldo cuenta=",saldo_cuenta)
            print("saldo cajero=",saldo_cajero,)
            break
        else:
            print("monto no permitido")
            break

    else:
        print("clave inválida")
        intentos=(int(intentos-1))
        if intentos==0:
            print("Tarjeta bloqueada")
            break

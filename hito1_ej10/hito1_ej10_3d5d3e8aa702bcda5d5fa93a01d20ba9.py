#Cajero Automático
saldo_cajero=1000000
saldo_cuenta=100000
intentos=3
while intentos>0:
    usuario=int(input("Ingrese su usuario "))
    clave=int(input("ingrese su clave de cuatro digitos ")) 
    if usuario==10334151 and clave==1803:
        print("Clave y usuario valido")
        monto_retirar=int(input("Ingrese su monto a retirar: "))
        if monto_retirar<=100000:
            print("saldo cuenta=",saldo_cuenta-monto_retirar)
            print("saldo cajero=",saldo_cajero-monto_retirar)
            break
        elif monto_retirar>saldo_cajero or monto_retirar>saldo_cuenta:
            print("monto no permitido")
        t=input("Para salir ingrese algo distinto de N: ")
        if t!=N:
            break
           
    elif usuario!=10334151 or clave!=1803:
        print("Incorrecto, ingrese nuevamente")
        intentos=intentos-1
    else:
        print("Tarjeta bloqueada")

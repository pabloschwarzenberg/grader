#Cajero Automático

saldo_cajero=1000000
usuario=10334151
clavereal=1803
saldo_usuario=100000

usuario1=int(input("ingrese numero de usuario: "))
intentos=0
if usuario1==usuario:
    while intentos <=2:
        clave=int(input("Ingrese clave: "))
        if clave!=clavereal:
            print("clave invalida, ingrese nuevamente ")
        else:
            monto=int(input("¿Cual es el monto a retirar? :"))
            if monto>saldo_usuario :
                print("monto no permitido ")
            else:
                saldo_usuario=saldo_usuario-monto
                saldo_cajero=saldo_cajero-monto
                print("saldo cuenta="+str(saldo_usuario))
                print("saldo cajero="+str(saldo_cajero))
            break
        intentos=intentos+1
if intentos==2:
    print("tarjeta bloqueada")
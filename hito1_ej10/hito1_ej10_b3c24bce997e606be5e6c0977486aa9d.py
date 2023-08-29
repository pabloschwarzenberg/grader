#Cajero Automático
saldo_cajero=1000000
saldo_inicial=100000
saldo=0
intentos=2
clave=int(input("ingrese la contraseña: "))
while intentos != 0:
    if clave != 1803:
        print("clave incorrecta")
        intentos=intentos-1
        clave=int(input("ingrese la contraseña: "))
    else:
        monto=int(input("ingrese monto que quiera retirar: "))
        if monto < saldo_inicial:
            saldo=saldo_inicial-monto
            saldo_cajero=saldo_cajero-monto
            print("saldo cuenta=", saldo)
            print("saldo cajero=", saldo_cajero)
            break
        else:
            print("monto no permitido")
if intentos==0:
    print("tarjeta bloqueada")
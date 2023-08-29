#Cajero Automático
saldo_cajero=1000000
saldo_inicial=100000
saldo=0
intentos=2

clave=int(input("Ingrese su password: "))

while intentos != 0:
    if clave != 1803:
        print("clave invalida")
        intentos=intentos-1
        clave=int(input("Ingrese su password: "))
    else:
        monto=int(input("Ingrese el monto que deseas retirar de tu cuenta (sin puntos): "))
        if monto < saldo_inicial:
            saldo=saldo_inicial-monto
            saldo_cajero=saldo_cajero-monto
            print("saldo cuenta=", saldo)
            print("saldo cajero=", saldo_cajero)
            break
        else:
            print("monto no permitido")
if intentos==0:
    print("Ha bloqueado su tarjeta")      
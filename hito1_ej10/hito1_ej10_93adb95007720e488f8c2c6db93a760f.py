#Cajero Automático
saldo_cajero = 1000000
saldo_inicial = 100000
saldo=0
intentos=2

clave=int(input("Ingrese su contraseña: "))

while intentos != 0:
    if clave != 1803:
        print("Clave inválida")
        intentos -= 1
        clave = int(input("Vuelva a ingresar su contraseña: "))
    else:
        monto = int(input("Ingrese el monto a retirar de su cuenta: "))
        if monto < saldo_inicial:
            saldo = saldo_inicial - monto
            saldo_cajero =saldo_cajero - monto
            print("Saldo cuenta=", saldo)
            print("Saldo cajero=", saldo_cajero)
            break
        else:
            print("Monto no permitido")
if intentos==0:
    print("tarjeta bloqueada")       
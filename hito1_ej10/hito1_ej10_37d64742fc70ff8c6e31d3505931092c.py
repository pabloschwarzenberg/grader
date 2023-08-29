#Cajero Automatico

saldo_cajero = 1000000
saldo_usuario = 100000
suma = 0
usuario = input("Ingrese usuario: " )
while True:
    if usuario == "10334151":
        clave = input("ingrese clave: ")
        if clave == "1803":
            retiro = int(input("Monto a retirar: "))
            if 0 < retiro < saldo_usuario:
                saldo_cuenta = saldo_usuario - retiro
                saldo_cajero_final = saldo_cajero - retiro
                print("saldo cuenta=",saldo_cuenta)
                print("saldo cajero=",saldo_cajero_final)
                break
            else:
                print("monto no permitido")
                break
        else:
            if suma == 2:
                print("tarjeta bloqueada")
                break
            else:
                print("clave invalida")
                suma += 1
    else:
        usuario = input("Ingrese usuario: " )

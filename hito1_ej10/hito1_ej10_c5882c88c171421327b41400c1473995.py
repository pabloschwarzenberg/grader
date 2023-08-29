#cajero 1
saldo_cajero = 1000000
intentos = 3

usuario = 10334151
saldo_usuario = 100000
clave_usuario =1803

while intentos > 0:
    ingrese = int(input("ingrese usuario"))
    ingrese_clave = int(input("ingrese clave"))
    if ingrese != usuario or ingrese_clave != clave_usuario:
        print("clave invalida")
        intentos-=1
    else:
        break

    if intentos == 0:
        print("tarjeta bloqueada")
    else:
        while True:
            monto =input(int("monto"))
            if monto == "N":
                break
            else:
                if int(monto) > saldo_usuario or int(monto) > saldo_cajero:
                    print("monto no permitido")
                else:
                    saldo_usuario-= int(monto)
                    saldo_cajero-=int(monto)
print("saldo cuenta="+ str(saldo_usuario))
print("saldo cajero="+ str(saldo_cajero))
#Cajero Automático
saldo_inicial=1000000
saldo_cuenta=100000
intentos_clave=0


while intentos_clave < 4:
    usuario = int(input("Ingrese su usuario: "))
    clave = int(input("Ingrese  su clave: "))

    if usuario == 10334151 and clave == 1803:
        monto_retiro = int(input("Cuanto dinero desea retirar: "))
        if monto_retiro <= saldo_cuenta and monto_retiro != 0:
            saldo_res_cuenta = saldo_cuenta - monto_retiro
            saldo_res_cajero = saldo_inicial - monto_retiro
            print("Saldo cuenta = "+str(saldo_res_cuenta))
            print("Saldo cajero = "+str(saldo_res_cajero))
            break
        else:
            print("Monto no permitido")
            

    else:
        print("Clave invalida")
        intentos_clave = intentos_clave+1
        print(intentos_clave)
        if intentos_clave == 3:
            print("Tarjeta bloqueada")
            break
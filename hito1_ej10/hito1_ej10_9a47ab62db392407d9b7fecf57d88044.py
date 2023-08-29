#Cajero Automático
saldo_cajero= 1000000
usuario=10334151
clave = 1803
saldo_cuenta = 100000
monto_retiro=0
ingrese_usuario=0
clave_ingresada =0
intento= 0
while True:
    ingrese_usuario=int(input("ingrese usuario:"))
    clave_ingresada = int(input("ingrese su clave:"))
    
    if clave != clave_ingresada:
        print("clave invalida")
        intento + 1
    if intento>3:
        break
    if clave==clave_ingresada:
        monto_retiro=int(input("ingrese monto a retirar:"))
        if monto_retiro>saldo_cuenta:
            print("monto no permitido")
        if monto_retiro<=saldo_cuenta:
            break
        
if monto_retiro<saldo_cuenta:
    saldo_final_cuenta=saldo_cuenta - monto_retiro
    saldo_final_cajero = saldo_cajero - monto_retiro
    print("saldo cuenta=",saldo_final_cuenta)
    print("saldo cajero=",saldo_final_cajero)
    
if intento>3:
    print("tarjeta bloqueada")
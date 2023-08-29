#Cajero Automático
saldo_cajero= 1000000
usuario=10334151
clave = 1803
saldo_cuenta = 100000
monto_retiro=0
ingrese_usuario=0
clave_ingresada =0
intento= 0
billetes20 =20
billetes10 =40
billetes5 =40
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
if monto_retiro>=20000:
    division = monto_retiro//20000
    billetes20 = division
    resto = monto_retiro%20000
    division2 = resto//10000
    billetes10 = division2
    resto2 = resto%10000
    division3 = resto2//5000
    billetes5 = division3
if monto_retiro<20000 and monto_retiro>=10000:
    division = monto_retiro//10000
    billetes10 = division
    resto = monto_retiro % 10000
    division2 = resto//5000
    billetes5 = division2
    billetes20 = 0
if monto_retiro<10000 and monto_retiro>=5000:
    division = monto_retiro//5000
    billetes5 = division
    billetes20=0
    billetes10 =0

print("billetes 20000=",billetes20)
print("billetes 10000=",billetes10)
print("billetes 5000=",billetes5)

    
if intento>3:
    print("tarjeta bloqueada")
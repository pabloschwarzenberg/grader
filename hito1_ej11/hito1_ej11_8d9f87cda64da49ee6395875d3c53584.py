#Cajero Automático
contador = 1
while contador <=3:
    usuario = int(input("Codigo de usuario: "))
    contraseña = int(input("Contraseña:"))
    if usuario == 10334151 and contraseña == 1803:
        contador = 4
        pass
    else:
        print("clave invalida")
        if contador == 3:
            exit("tarjeta bloqueada")
        contador = contador + 1
print("Su saldo es $100.000")
print("Escriba monto sin puntos ni comas")
monto_a_retirar = int(input("Cuanto dinero desea retirar: "))
if monto_a_retirar > 100000 and monto_a_retirar < 5000:
    print("monto no permitido")
elif monto_a_retirar < 100000:
    saldo_nuevo_cuenta = 100000 - monto_a_retirar
    saldo_nuevo_cajero = 1000000 - monto_a_retirar
    print("saldo cuenta=",saldo_nuevo_cuenta)
    print("saldo cajero=",saldo_nuevo_cajero)
    if monto_a_retirar == 5000:
        print("billetes 5000=1")
    elif monto_a_retirar == 10000:
        print("billetes 10000=1")
    elif monto_a_retirar == 15000:
        print("billetes 10000=1")
        print("billetes 5000=1")
    elif monto_a_retirar == 20000:
        print("billetes 20000=1")
    elif monto_a_retirar == 25000:
        print("billetes 20000=1")
        print("billetes 5000=1")
    elif monto_a_retirar == 30000:
        print("billetes 20000=1")
        print("billetes 10000=1")
    elif monto_a_retirar == 35000:
        print("billetes 20000=1")
        print("billetes 10000=1")
        print("billetes 5000=1")
    elif monto_a_retirar == 40000:
        print("billetes 20000=2")
    elif monto_a_retirar == 45000:
        print("billetes 20000=2")
        print("billetes 5000=1")
    elif monto_a_retirar == 50000:
        print("billetes 20000=2")
        print("billetes 10000=1")
    elif monto_a_retirar == 55000:
        print("billetes 20000=2")
        print("billetes 10000=1")
        print("billetes 5000=1")
    elif monto_a_retirar == 60000:
        print("billetes 20000=3")
    elif monto_a_retirar == 65000:
        print("billetes 20000=3")
        print("billetes 5000=1")
    elif monto_a_retirar == 70000:
        print("billetes 20000=3")
        print("billetes 10000=1")
    elif monto_a_retirar == 75000:
        print("billetes 20000=3")
        print("billetes 10000=1")
        print("billetes 5000=1")
    elif monto_a_retirar == 80000:
        print("billetes 20000=4")
    elif monto_a_retirar == 85000:
        print("billetes 20000=4")
        print("billetes 5000=1")
    elif monto_a_retirar == 90000:
        print("billetes 20000=4")
        print("billetes 10000=1")
    elif monto_a_retirar == 95000:
        print("billetes 20000=4")
        print("billetes 10000=1")
        print("billetes 5000=1")
    elif monto_a_retirar == 100000:
        print("billetes 20000=5")
    else:
        print("")
 
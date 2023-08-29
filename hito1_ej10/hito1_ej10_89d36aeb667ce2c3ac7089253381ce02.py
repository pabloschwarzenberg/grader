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
if monto_a_retirar > 100000:
    print("monto no permitido")
elif monto_a_retirar < 100000:
    saldo_nuevo_cuenta = 100000 - monto_a_retirar
    saldo_nuevo_cajero = 1000000 - monto_a_retirar
    print("saldo cuenta=",saldo_nuevo_cuenta)
    print("saldo cajero=",saldo_nuevo_cajero)
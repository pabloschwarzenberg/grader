def verificar_clave(usuario, clave):
    if usuario == "10334151" and clave == "1803":
        return True
    else:
        return False

saldo_cuenta = 100000
saldo_cajero = 1000000

usuario = "10334151"
clave = "1803"
monto_retiro = 45000

if verificar_clave(usuario, clave):
    if monto_retiro <= saldo_cuenta and monto_retiro > 0:
        saldo_cuenta -= monto_retiro
        saldo_cajero -= monto_retiro
        print("Retiro exitoso.")
    else:
        print("Monto no permitido.")

    print("Saldo cuenta =", saldo_cuenta)
    print("Saldo cajero =", saldo_cajero)
else:
    print("Clave inválida.")

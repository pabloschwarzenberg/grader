saldo_cuenta = 100000
saldo_cajero = 1000000

intentos = 0

usuario = "10334151"
clave = "1803"

while True:
    print("Ingrese su usuario: ", usuario)
    print("Ingrese su clave: ", clave)

    if usuario == "10334151" and clave == "1803":
        print("Inicio de sesión exitoso.")
        break
    else:
        intentos += 1
        print("Clave inválida.")

    if intentos == 3:
        print("Tarjeta bloqueada.")
        exit()

monto = 45000

if monto <= 0:
    print("Monto no permitido.")
elif monto > saldo_cuenta:
    print("Saldo insuficiente.")
elif monto > saldo_cajero:
    print("Cajero sin suficiente dinero.")
else:
    saldo_cuenta -= monto
    saldo_cajero -= monto
    print("Retiro exitoso.")
    print("Saldo cuenta=", saldo_cuenta)
    print("Saldo cajero=", saldo_cajero)

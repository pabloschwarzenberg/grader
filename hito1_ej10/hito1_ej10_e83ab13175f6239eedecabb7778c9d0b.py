#Cajero Automático
saldo_cuenta = 100000
saldo_cajero = 1000000
intentos_fallidos = 0

usuario = "10334151" 
clave = "1803"  

if usuario == "10334151" and clave == "1803":
    print("Bienvenido/a,", usuario)
else:
    print("Clave inválida")
    exit()

monto_retiro = 45000  

if monto_retiro % 5000 != 0:
    print("Monto no permitido. El monto debe ser múltiplo de 5000.")
elif monto_retiro > saldo_cuenta:
    print("Monto no permitido. Saldo insuficiente.")
else:
    saldo_cuenta -= monto_retiro
    saldo_cajero -= monto_retiro

    print("Retiro exitoso. Saldo cuenta =", saldo_cuenta)
    print("Saldo cajero =", saldo_cajero)

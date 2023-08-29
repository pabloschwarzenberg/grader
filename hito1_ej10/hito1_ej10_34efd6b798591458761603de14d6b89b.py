#Cajero Automático
def validar_clave(usuario, clave):
    if usuario == 10334151 and clave == 1803:
        return True
    else:
        return False

def retirar_dinero(saldo, monto):
    if monto <= saldo:
        saldo -= monto
        return saldo
    else:
        return -1

saldo_cuenta = 100000
saldo_cajero = 1000000
intentos = 0

while True:
    usuario = int(input("Ingrese su número de usuario: "))
    clave = int(input("Ingrese su clave: "))

    if validar_clave(usuario, clave):
        print("Clave válida. Bienvenido.")
        break
    else:
        print("Clave inválida.")
        intentos += 1

    if intentos >= 3:
        print("Tarjeta bloqueada.")
        exit()

while True:
    monto_retiro = int(input("Ingrese el monto a retirar: "))

    if monto_retiro <= 0:
        print("Monto no permitido.")
        continue

    nuevo_saldo = retirar_dinero(saldo_cuenta, monto_retiro)

    if nuevo_saldo == -1:
        print("Saldo insuficiente.")
    else:
        saldo_cuenta = nuevo_saldo
        saldo_cajero -= monto_retiro
        print("Saldo cuenta =", saldo_cuenta)
        print("Saldo cajero =", saldo_cajero)

    continuar = input("¿Desea realizar otro retiro? (S/N): ")
    if continuar.upper() != "S":
        break
    
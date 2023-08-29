#Cajero Automático
import sys

saldo_cuenta = 100000
saldo_cajero = 1000000

usuario_valido = "10334151"
clave_valida = "1803"
intentos_fallidos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == usuario_valido and clave == clave_valida:
        break
    else:
        print("Clave inválida.")
        intentos_fallidos += 1

        if intentos_fallidos == 3:
            print("Tarjeta bloqueada.")
            sys.exit()

while True:
    try:
        monto_retiro = float(sys.stdin.readline().strip())

        if monto_retiro > 0:
            if monto_retiro <= saldo_cuenta:
                saldo_cuenta -= monto_retiro
                saldo_cajero -= monto_retiro
                print("Retiro exitoso.")
                print("Saldo cuenta =", saldo_cuenta)
                print("Saldo cajero =", saldo_cajero)
            else:
                print("Monto no permitido. Saldo insuficiente.")
        else:
            print("Monto no permitido.")

        opcion = input("¿Desea realizar otro retiro? (N para salir): ")
        if opcion.upper() == "N":
            break
    except ValueError:
        print("Monto inválido. Ingrese un número válido.")

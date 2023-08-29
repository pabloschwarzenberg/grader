#Cajero Automático
saldo_inicial = 1000000
saldo_cajero = 1000000

usuario_valido = 10334151
clave_valida = 1803

intentos = 0
bloqueado = False

while True:
    usuario = int(input("Ingrese su usuario: "))
    clave = int(input("Ingrese su clave: "))

    if bloqueado:
        print("Tarjeta bloqueada")
        break

    if usuario == usuario_valido and clave == clave_valida:
        saldo_cuenta = 100000
        print("Bienvenido/a")
        break
    else:
        print("Clave inválida")
        intentos += 1

    if intentos == 3:
        bloqueado = True

while True:
    if bloqueado:
        print("Tarjeta bloqueada")
        break

    monto_retiro = int(input("Ingrese el monto a retirar: "))

    if monto_retiro <= 0:
        print("Monto no permitido")
    elif monto_retiro > saldo_cuenta:
        print("Saldo insuficiente")
    else:
        saldo_cuenta -= monto_retiro
        saldo_cajero -= monto_retiro
        print("Saldo cuenta =", saldo_cuenta)
        print("Saldo cajero =", saldo_cajero)

    opcion = input("¿Desea realizar otro retiro? (Ingrese 'N' para salir): ")
    if opcion != 'N' and opcion != 'n':
        break 
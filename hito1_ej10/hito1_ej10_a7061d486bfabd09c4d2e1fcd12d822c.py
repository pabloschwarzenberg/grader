# ----------
# Cajero Automático
# ----------

# Definir vairables
saldo_cajero = 1000000
saldo_tarjeta = 10000

clave = 0
intentos = 0

clave = int(input('Ingrese su contraseña:'))

# ----
# Verificar el valor de la contraseña
while clave != 1803 and intentos < 3:
    print('Clave inválida.')
    clave = int(input('Ingrese su contraseña:'))
    intentos += 1

    # ----
    # Si la contraseña es correcta, entrar al cajero
    if clave == 1803:
        retiro = int(input('Indique el monto a retirar: '))
        if retiro > saldo_cajero:
            print('Monto no permitido.')
        else:
            saldo_cajero = saldo_cajero - retiro
            saldo_tarjeta = saldo_tarjeta + retiro
            print("Saldo en el cajero: ", saldo_cajero)
            print("Saldo en el tarjeta: ", saldo_tarjeta)


if intentos >= 3:
    print('Tarjeta bloqueada.')
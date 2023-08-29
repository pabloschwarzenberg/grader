# Saldo inicial del cajero distribuido en billetes
billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

# Saldo inicial y datos de usuario
saldo_inicial = 1000000
usuario_valido = "10334151"
clave_valida = "1803"
saldo_usuario = 100000

# Contadores de intentos fallidos y bloqueo
intentos_fallidos = 0
bloqueado = False

# Función para calcular la cantidad de billetes necesarios
def calcular_billetes(monto):
    billetes_20000_retiro = min(monto // 20000, billetes_20000)
    monto -= billetes_20000_retiro * 20000

    billetes_10000_retiro = min(monto // 10000, billetes_10000)
    monto -= billetes_10000_retiro * 10000

    billetes_5000_retiro = min(monto // 5000, billetes_5000)
    monto -= billetes_5000_retiro * 5000

    return billetes_20000_retiro, billetes_10000_retiro, billetes_5000_retiro

# Bucle principal del programa
while True:
    # Solicitar usuario y clave
    usuario = input("Usuario: ")
    clave = input("Clave: ")

    # Verificar clave y bloqueo
    if usuario == usuario_valido and clave == clave_valida:
        if bloqueado:
            print("Tarjeta bloqueada. Contacte al banco.")
            break
        else:
            # Solicitar monto a retirar
            monto = float(input("Monto a retirar: "))

            # Verificar monto permitido
            if monto <= saldo_usuario:
                # Verificar disponibilidad de billetes
                if monto <= (billetes_20000 * 20000 + billetes_10000 * 10000 + billetes_5000 * 5000):
                    # Calcular cantidad de billetes necesarios para el retiro
                    billetes_20000_retiro, billetes_10000_retiro, billetes_5000_retiro = calcular_billetes(monto)

                    # Actualizar saldos de billetes
                    billetes_20000 -= billetes_20000_retiro
                    billetes_10000 -= billetes_10000_retiro
                    billetes_5000 -= billetes_5000_retiro

                    # Actualizar saldo del usuario
                    saldo_usuario -= (billetes_20000_retiro * 20000 +
                                      billetes_10000_retiro * 10000 +
                                      billetes_5000_retiro * 5000)

                    # Imprimir billetes entregados y saldos actualizados
                    print("Billetes 20000:", billetes_20000_retiro)
                    print("Billetes 10000:", billetes_10000_retiro)
                    print("Billetes 5000:", billetes_5000_retiro)
                    print("Saldo cuenta:", saldo_usuario)
                    print("Saldo cajero:", billetes_20000 * 20000 +
                                           billetes_10000 * 10000 +
                                           billetes_5000 * 5000)
                else:
                    print("No

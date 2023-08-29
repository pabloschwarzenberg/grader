#Cajero Automático
  saldo_inicial = 1000000
saldo_usuario = 100000
intentos_fallidos = 0
usuario_valido = "10334151"
clave_valida = "1803"

while True:
    usuario = input("Ingrese el número de usuario: ")
    clave = input("Ingrese la clave: ")

    if usuario == usuario_valido and clave == clave_valida:
        while True:
            monto_retiro = float(input("Ingrese el monto a retirar: "))

            if monto_retiro <= saldo_usuario and monto_retiro <= saldo_inicial:
                saldo_usuario -= monto_retiro
                saldo_inicial -= monto_retiro
                print(f"Retiro exitoso. Saldo cuenta: {saldo_usuario}. Saldo cajero: {saldo_inicial}")
            else:
                print("Monto no permitido")

            opcion = input("¿Desea realizar otro retiro? (S/N): ")
            if opcion.upper() != "S":
                break
    else:
        intentos_fallidos += 1
        print("Clave inválida.")

    if intentos_fallidos == 3:
        print("Tarjeta bloqueada.")
        break

    opcion = input("¿Desea realizar otra transacción? (S/N): ")
    if opcion.upper() != "S":
        break
    
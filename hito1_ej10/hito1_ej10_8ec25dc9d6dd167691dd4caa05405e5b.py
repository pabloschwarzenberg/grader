saldo_cajero = 1000000
saldo_usuario = 100000
usuario_valido = "10334151"
clave_valida = "1803"
intentos_fallidos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == usuario_valido and clave == clave_valida:
        intentos_fallidos = 0
        monto = float(input("Ingrese el monto a retirar: "))

        if monto <= saldo_usuario:
            saldo_usuario -= monto
            saldo_cajero -= monto
            print("Saldo cuenta =", saldo_usuario)
            print("Saldo cajero =", saldo_cajero)
        else:
            print("Monto no permitido")
    else:
        intentos_fallidos += 1
        print("Clave inválida")

        if intentos_fallidos == 3:
            print("Tarjeta bloqueada")
            break

    continuar = input("¿Desea realizar otra transacción? (S/N): ")
    if continuar != "S" and continuar != "s":
        break
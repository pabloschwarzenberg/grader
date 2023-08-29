#Cajero Automático
saldo_cuenta = 100000
saldo_cajero = 1000000
intentos = 0

usuario = "10334151"
clave = "1803"

while True:
    if intentos == 3:
        print("Tarjeta bloqueada.")
        break

    ingreso_usuario = input("Ingrese su usuario: ")
    ingreso_clave = input("Ingrese su clave: ")

    if ingreso_usuario == usuario and ingreso_clave == clave:
        print("Bienvenido")
        break
    else:
        print("Usuario o clave incorrectos.")
        intentos += 1

while True:
    try:
        monto_retiro = 45000  # Puedes ajustar este valor según tus necesidades
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número válido.")
        continue

    if monto_retiro <= saldo_cuenta and monto_retiro <= saldo_cajero:
        saldo_cuenta -= monto_retiro
        saldo_cajero -= monto_retiro
        print("Retiro exitoso.")
        print("Saldo cuenta =", saldo_cuenta)
        print("Saldo cajero =", saldo_cajero)
    else:
        print("Monto no permitido.")

    continuar = input("¿Desea realizar otro retiro? (N para salir): ")
    if continuar.upper() == "N":
        break

  

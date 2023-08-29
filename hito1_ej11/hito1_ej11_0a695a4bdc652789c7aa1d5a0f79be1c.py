saldo_cuenta = 100000
saldo_cajero = 1000000
intentos = 0

# Valores predefinidos para el número de cuenta y la clave
usuario_correcto = "10334151"
clave_correcta = "1803"

# Cantidad de billetes disponibles
billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

# Solicitar al usuario el número de cuenta y la clave
usuario = input("Ingrese su número de cuenta: ")
clave = input("Ingrese su clave: ")

while usuario != usuario_correcto or clave != clave_correcta:
    intentos += 1

    if intentos == 3:
        print("Tarjeta bloqueada. Demasiados intentos fallidos.")
        exit()
    
    print("Clave inválida. Intente nuevamente.")
    usuario = input("Ingrese su número de cuenta: ")
    clave = input("Ingrese su clave: ")

print("Inicio de sesión exitoso.")

monto = float(input("Ingrese el monto a retirar: "))

if monto <= saldo_cuenta and monto > 0:
    # Verificar si hay suficientes billetes de cada denominación
    if monto > billetes_20000 * 20000 + billetes_10000 * 10000 + billetes_5000 * 5000:
        print("No hay suficientes billetes disponibles.")
    else:
        # Calcular la cantidad de billetes de cada denominación a entregar
        cant_billetes_20000 = min(monto // 20000, billetes_20000)
        monto -= cant_billetes_20000 * 20000
        billetes_20000 -= cant_billetes_20000
        
        cant_billetes_10000 = min(monto // 10000, billetes_10000)
        monto -= cant_billetes_10000 * 10000
        billetes_10000 -= cant_billetes_10000
        
        cant_billetes_5000 = min(monto // 5000, billetes_5000)
        monto -= cant_billetes_5000 * 5000
        billetes_5000 -= cant_billetes_5000
        
        saldo_cuenta -= (monto + cant_billetes_20000 * 20000 + cant_billetes_10000 * 10000 + cant_billetes_5000 * 5000)
        saldo_cajero -= (cant_billetes_20000 * 20000 + cant_billetes_10000 * 10000 + cant_billetes_5000 * 5000)
        
        print("Retiro exitoso.")
        print("Saldo cuenta =", saldo_cuenta)
        print("Saldo cajero =", saldo_cajero)
        print("Billetes 20000 =", int(cant_billetes_20000))
        print("Billetes 10000 =", int(cant_billetes_10000))
        print("Billetes 5000 =", int(cant_billetes_5000))
else:
    print("Monto no permitido.")

print("Gracias por utilizar nuestro cajero automático.")


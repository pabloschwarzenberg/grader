saldo_cuenta = 100000
saldo_cajero = 1000000
intentos = 0

# Valores predefinidos para el número de cuenta y la clave
usuario_correcto = "10334151"
clave_correcta = "1803"

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
    saldo_cuenta -= monto
    saldo_cajero -= monto
    print("Retiro exitoso.")
    print("Saldo cuenta=" + str(saldo_cuenta))
    print("Saldo cajero=" + str(saldo_cajero))
else:
    print("Monto no permitido.")

print("Gracias por utilizar nuestro cajero automático.")

# Crear una cuenta corriente
cuenta = CuentaCorriente("123456789", 1000)

# Hacer un giro
resultado = cuenta.girar(500)
print(resultado)  # Salida: True
print(cuenta.saldo)  # Salida: 500

# Intentar hacer otro giro con saldo insuficiente
resultado = cuenta.girar(1000)
print(resultado)  # Salida: False
print(cuenta.saldo)  # Salida: 500

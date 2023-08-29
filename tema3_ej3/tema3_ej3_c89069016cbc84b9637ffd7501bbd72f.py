# Crear una instancia de CuentaCorriente
cuenta = CuentaCorriente("123456789", 10000)

# Realizar un giro de 5000
if cuenta.girar(5000):
    print("Giro exitoso.")
else:
    print("Fondos insuficientes.")

# Verificar el saldo actual
print("Saldo:", cuenta.saldo)

# Intentar realizar un giro mayor al saldo disponible
if cuenta.girar(8000):
    print("Giro exitoso.")
else:
    print("Fondos insuficientes.")

# Verificar el saldo actual
print("Saldo:", cuenta.saldo)

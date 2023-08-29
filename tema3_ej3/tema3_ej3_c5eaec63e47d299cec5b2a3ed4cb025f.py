# Crear una instancia de la clase CuentaCorriente
cuenta = CuentaCorriente("123456789", 1000)

# Realizar un giro de 500
puede_girar = cuenta.girar(500)
if puede_girar:
    print("Giro exitoso")
    print("Nuevo saldo:", cuenta.saldo)
else:
    print("Saldo insuficiente")

#operaciones
puede_girar = cuenta.girar(1000)
if puede_girar:
    print("Giro exitoso")
    print("Nuevo saldo:", cuenta.saldo)
else:
    print("Saldo insuficiente")

cuenta = CuentaCorriente("12345678-9", 1000)  # Crear una cuenta con rut "12345678-9" y saldo inicial de 1000
print(cuenta.girar(500))  # Intentar girar 500 (debería retornar True)
print(cuenta.saldo)  # Imprimir el saldo actual de la cuenta (debería ser 500)

print(cuenta.girar(1000))  # Intentar girar 1000 (debería retornar False)
print(cuenta.saldo)  # Imprimir el saldo actual de la cuenta (debería seguir siendo 500)

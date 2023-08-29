cuenta_1 = CuentaCorriente("12864303-6", 10000)
monto_giro = 5000
if cuenta_1.girar(monto_giro):
    print("Giro realizado con éxito.")
else:
    print("Saldo insuficiente para realizar el giro.")

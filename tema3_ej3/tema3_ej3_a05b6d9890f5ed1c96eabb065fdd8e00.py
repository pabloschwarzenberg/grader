cuenta_1 = CuentaCorriente("12864303-6", 10000)
print(cuenta_1.girar(5000))  # True
print(cuenta_1.saldo)  # 5000

print(cuenta_1.girar(10000))  # False
print(cuenta_1.saldo)  # 5000

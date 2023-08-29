numero = int(input("ingrese su numero: "))

umil = numero // 1000
tmp = numero % 1000

centenas = tmp // 100
tmp = tmp % 100

decenas = tmp // 10
unidades = tmp % 10

print(umil,"M", "+", centenas,"C", "+", decenas,"D", "+", unidades,"U")
#Conversión de Decimal a Binario
n_decimal = int(input("ingrese un número decimal : "))

n_binario = ""

while n_decimal > 0:
  resto = n_decimal % 2
  n_decimal = int(n_decimal/2)
  n_binario = str(resto) + n_binario

print("resultado= ", n_binario)

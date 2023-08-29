#Conversión de Decimal a Binario
print("Decimal a binario")
n = int(input("ingrese un numero: "))
b = ""
print("el numero escogido es: " , n)
while n > 0:
  resto = n % 2
  n = n // 2
  b = str(resto) + b
print("resultado = " , b)
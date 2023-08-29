#Conversión de Decimal a Binario
x=int(input("ingresa un numero decimil: "))
bin = ""

while x > 0:
  resto = int(x % 2)
  x = int(x/2)
  bin = str(resto) + bin

print("resultado=",bin)      
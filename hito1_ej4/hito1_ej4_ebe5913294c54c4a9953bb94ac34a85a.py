#Conversión de Decimal a Binario
n = eval(input("Ingrese número decimal: "))
forma_binario = ""
#División para ver si es impar o par
while n > 1:
  resn = n % 2
  n = n // 2
  if resn == 0:
    forma_binario += "0"
    continue
  else:
    forma_binario += "1"
    continue
forma_binario += "1"
print("resultado=" + forma_binario[::-1])
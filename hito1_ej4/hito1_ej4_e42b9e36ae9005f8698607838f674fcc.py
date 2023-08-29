#Conversión de Decimal a Binario
x = int(input(""))
i = x
TempA = ""
while i != 0:
  TempA = str(i % 2) + TempA
  i = int(i / 2)
print("resultado=" + TempA)

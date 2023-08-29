#Descomponer un número
numero=int(input("ingrese un número de hasta 4 dígitos:"))
miles=numero//1000
centena=(numero//100)%10
decena=(numero//10)%10
unidad=(numero//1)%10
print(unidad)
print(decena)
print(centena)
print(miles)
if (1<=numero<=9):
  print(unidad,"U")
elif (10<=numero<=99):
  print(decena,"D +",unidad,"U")
elif (100<=numero<=999):
  print(centena,"C +",decena,"D +",unidad,"U")
else:
  print(miles,"M +",centena,"C +",decena,"D +",unidad,"U")
#Descomponer un número
numero = int(input())
i = 1
unidades = 0
decenas = 0
centenas = 0
miles = 0
while numero:
  digito = numero % 10
  if i == 1:
    unidades = digito
  if i == 2:  
    decenas = digito
  if i == 3:
    centenas = digito
  if i == 4:
    miles = digito
  i = i + 1  
  numero //= 10
if miles != 0:
    print(miles,"M +",centenas,"C +",decenas,"D +",unidades,"U")
elif miles == 0 and centenas != 0:
    print(centenas,"C +",decenas,"D +",unidades,"U")
elif miles == 0 and centenas == 0 and decenas != 0:
    print(decenas,"D +",unidades,"U")
elif miles == 0 and centenas == 0 and decenas == 0 and unidades != 0:
    print(unidades,"U")







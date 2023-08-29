a=int(input("Ingrese un número"))
miles=a//1000
centenas=(a-(1000*miles))//100
decenas=(a-(1000*miles)-(100*centenas))//10
unidades=(a-(1000*miles)-(100*centenas)-(10*decenas))//1

if a>999:
          print(miles,"M +",centenas, "C +",decenas,"D +",unidades,"U")

if 99<a<=999:
          print(centenas,"C +",decenas,"D +",unidades,"U")

if 9<a<=99:
          print(decenas,"D +",unidades,"U")

if 0<=a<=9:
          print(unidades,"U")


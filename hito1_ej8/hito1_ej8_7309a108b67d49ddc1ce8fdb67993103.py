numero=int(input("ingrese un numero de hasta 4 digitos:"))
unidad=(numero%10)
decena=(numero//10)%10
centena=(numero//100)%10 
miles=numero//1000

if(10<=numero<=99):
  print(decena,"D +",unidad,"U")
elif(100<=numero<=999):
  print(centena,"C +",decena,"D +",unidad,"U")
else:
  print(miles,"M +",centena,"C +",decena,"D +",unidad,"U")

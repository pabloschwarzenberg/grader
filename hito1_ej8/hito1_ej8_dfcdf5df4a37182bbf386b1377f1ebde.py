n=int(input())
unidades=n%10
decenas=(n%100)//10
centenas=(n%1000)//100
miles=(n%10000)//1000
if decenas==0 and centenas==0 and miles==0:
  print(unidades,"U")
elif centenas==0 and miles==0:
  print(decenas,"D +",unidades,"U")
elif miles==0:
  print(centenas,"C +",decenas,"D +",unidades,"U")
else:
  print(miles,"M +",centenas,"C +",decenas,"D +",unidades,"U")
 
m=int(input("Ingrese numero: "))
millar=m//1000
m=m%1000
centena=m//100
m=m%100
decena=m//10
m=m%10
unidad=m
if millar!=0 and centena!=0 and decena!=0:
  print(millar,"M+",centena,"C+",decena,"D+",unidad,"U")
if millar==0 and centena!=0 and decena!=0:
  print(centena,"C+",decena,"D+",unidad,"U")
if millar==0 and centena==0 and decena!=0:
  print(decena,"D+",unidad,"U")
if millar==0 and centena==0 and decena==0:
  print(unidad,"U")
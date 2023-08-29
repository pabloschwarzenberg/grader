#Descomponer un número
n=int(input("Ingrese número: "))
milesima=(n%10000-n%1000)//1000
centena=(n%1000-n%100)//100
decena=(n%100-n%10)//10
unidad=n%10
if(milesima==0 and centena==0 and decena==0 and unidad>=0):
  print(unidad, "U")
elif(milesima==0 and centena==0 and decena>=0 and unidad>=0):
  print(decena,"D","+",unidad,"U")
elif(milesima==0 and centena>=0 and decena>=0 and unidad>=0):
  print(centena,"C","+",decena,"D","+",unidad,"U")

else: 
  print(milesima,"M","+",centena,"C","+",decena,"D","+",unidad,"U")
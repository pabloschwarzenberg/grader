#Descomponer un número
numero=int(input("ingrese un numero que tenga como maximo 4 digitos: "))
unidad=(numero%10)
decena=(numero%100-numero%10)//10
centena=(numero%1000-numero%100)//100
milesima=(numero%10000-numero%1000)//1000

if (numero>=1000):
  print(milesima,"M","+",centena,"C","+",decena,"D","+",unidad,"U")
  
elif (numero>=100 or numero<=999):
  print(centena,("C"),"+",decena,("D"),"+",unidad,("U"))
  
elif (numero>=10 or numero<=99):
  print(decena,("D"),"+",unidad,("U"))
  
elif (numero>=0 or numero<=9):
  print(unidad,("U"))
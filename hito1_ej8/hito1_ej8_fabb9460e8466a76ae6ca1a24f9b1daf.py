#Gustavo Altez irarrazabal
numero=int(input("ingrese un numero de hasta 4 caracteres: "))
U=numero%10
D=(numero%100)//10
C=(numero//100)%10
M=(numero//1000)
if numero>=1000:
  print(M,"M", " + ",C,"C"," + ",D,"D"," + ",U,"U")
if numero>=100 and numero<=999:
  print(C,"C"," + ",D,"D"," + ",U,"U")
if numero>=10 and numero<=99:
  print(D,"D"," + ",U,"U")
if numero>=0 and numero<=9:
  print(U,"U")
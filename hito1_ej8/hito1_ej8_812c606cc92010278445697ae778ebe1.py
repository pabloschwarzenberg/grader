#Descomponer un número
numero=int(input("Ingrese un numero de 4 cifras: "))
numero1=(numero//1000)
numero2=((numero//100)%10)
numero3=((numero//10)%10)
numero4=(numero%10)
if(numero>=0 and numero<10):
  print("",numero4,"U")
elif(numero>=10 and numero<=99):
  print ("",numero3,"D + ",numero4,"U")
elif(numero>=100 and numero<=999):
  print ("",numero2,"C + ",numero3,"D + ",numero4,"U")
elif(numero>=1000 and numero<=9999):
  print ("",numero1,"M + ",numero2,"C + ",numero3,"D + ",numero4,"U")
 
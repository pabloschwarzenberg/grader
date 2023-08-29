numero=int(input("Ingrese un numero de 4 cifras: "))
uno=(numero//1000)
dos=((numero//100)%10)
tres=((numero//10)%10)
cuatro=(numero%10)
if(numero>=0 and numero<10):
  print("",cuatro,"U")
elif(numero>=10 and numero<=99):
  print ("",tres,"D + ",cuatro,"U")
elif(numero>=100 and numero<=999):
  print ("",dos,"C + ",tres,"D + ",cuatro,"U")
elif(numero>=1000 and numero<=9999):
  print ("",uno,"M + ",dos,"C + ",tres,"D + ",cuatro,"U")
      
#Ordenar tres números
Numero1=int(input("ingrese el primer numero"))
Numero2=int(input("ingrese el segundo numero"))
Numero3=int(input("ingrese el tercero numero"))
if(Numero1<=Numero2 and Numero2<=Numero3):
  print("",Numero1," , ",Numero2," , ",Numero3)
elif(Numero2<=Numero1 and Numero1<=Numero3):
  print("",Numero2," , ",Numero1," , ",Numero3)
elif(Numero3<=Numero1 and Numero1<=Numero2):
  print("",Numero3," , ",Numero1," , ",Numero2)
elif(Numero3<=Numero2 and Numero2<=Numero1):
  print("",Numero3," , ",Numero2," , ",Numero1)
elif(Numero1<=Numero3 and Numero3<=Numero2):
  print("",Numero1," , ",Numero3," , ",Numero2)
elif(Numero2<=Numero3 and Numero3<=Numero1):
  print("",Numero2," , ",Numero3," , ",Numero1)  
#Ordenar tres números
Num1=int(input())
Num2=int(input())
Num3=int(input())
if(Num1<Num2<Num3):
  print(Num1,",",Num2,",",Num3)
elif(Num1>Num2>Num3):
  print(Num3,",",Num2,",",Num1)
elif(Num1<Num2>Num3) and (Num3>Num1):
  print(Num1,",",Num3,",",Num2)
elif(Num1<Num2>Num3) and (Num3<Num1):
  print(Num3,",",Num1,",",Num2)
elif(Num1>Num2<Num3) and (Num3>Num1):
  print(Num2,",",Num1,",",Num3)
elif(Num1>Num2<Num3) and (Num3<Num1):
  print(Num2,",",Num3,",",Num1)
elif(Num1<Num2) and (Num2==Num3):
  print(Num1,",",Num2,",",Num2)
elif(Num1>Num2) and (Num3==Num1):
  print(Num2,",",Num1,",",Num3)
elif(Num1==Num2>Num3):
  print(Num3,",",Num1,",",Num2)
elif(Num1==Num2<Num3):
  print(Num1,",",Num2,",",Num3)
elif(Num1<Num2) and (Num3==Num1):
  print(Num1,",",Num3,",",Num2)
elif(Num1>Num2==Num3):
  print(Num2,",",Num3,",",Num1)
elif(Num1==Num2==Num3):
  print(Num1,",",Num2,",",Num3)
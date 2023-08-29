#Descomponer un número
num=int(input("ingrese un numero: "))
num=str(num)
A=len(num)
if A==4:
   print(num[0],"M +",num[1],"C +",num[2],"D +",num[3],"U")
elif A==3:
   print(num[0],"C +",num[1],"D +",num[2],"U")
elif A==2:
   print(num[0],"D +",num[1],"U")
elif A==1:
   print(num[0],"U")
#Descomponer un número
num = int(input("Ingrese un numero:"))
m = (int(num)//1000)
c = (int(num)//100) - (int(num)//1000)*10
d = (int(num)//10) - (int(num)//100)*10
u = (int(num)%10)
if num <= 9:
  print("",u,"U")
elif num <= 99:
  print("",d,"D","+",u,"U")   
elif num <= 999:
  print("",c,"C","+","",d,"D","+",u,"U")  
elif num <= 9999:
  print("",m,"M","+","",c,"C","+","",d,"D","+",u,"U")
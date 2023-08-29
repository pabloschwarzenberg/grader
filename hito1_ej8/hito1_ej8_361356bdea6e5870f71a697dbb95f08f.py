n=int(input("Ingrese un numero hasta 4 digitos: "))
n1=n//1000
n2=(n%1000)//100
n3=(n%100)//10
n4=(n%10)
if(n1==0 and n2>0):
  print("",n2,"C +",n3,"D +",n4,"U")
if(n2==0 and n3>0):
  print("",n3,"D +",n4,"U")
if(n3==0 and n4>0):
  print("",n4,"U")
if(n1>0):
  print("",n1,"M +",n2,"C +",n3,"D +",n4,"U")
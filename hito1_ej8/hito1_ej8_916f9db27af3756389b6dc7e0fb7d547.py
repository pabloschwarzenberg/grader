#Descomponer un número
t=int(input("ingrese un valor hasta 4 digitos: "))
if(t<10):
  print(t,"U")
if(t<100):
  print(t//10,"D +",t%10,"U")
if(t<1000):
  print(t//100,"C +",(t//10)%10,"D +",t%10,"U")
if(t<10000):
  print(t//1000,"M +",(t//100)%10,"C +",(t%100)//10,"D +",t%10,"U")
if(t>=10000):
  print("lo sentimos, numero no valido")
#Descomponer un número
x=int(input("ingresa un número:"))
if(x>999):
  m=(x//1000)
  c=(x%1000)//100
  d=(x%100)//10
  u=(x%10)
  print(m,"M +",c,"C +",d,"D +",u,"U")
if(99<x<1000):
  c=(x//100)
  d=(x%100)//10
  u=(x%10)
  print(c,"C +",d,"D +",u,"U")
if(9<x<100):
  d=(x//10)
  u=(x%10)
  print(d,"D +",u,"U")
if(-1<x<10):
  u=(x)
  print(u,"U")
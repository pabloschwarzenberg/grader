#Descomponer un número
a=int(input("Inserte un número de hasta 4 dígitos: "))

u=int(a%10)
d=int((a%100)//10)
c=int((a%1000)//100)
m=int(a//1000)

if(a<10):
  print(u,"U")
  
elif(10<=a<100):
  print(d,"D +",u,"U")
  
elif(100<=a<1000):
  print(c,"C +",d,"D +",u,"U")
  
elif(1000<=a):
  print(m,"M +",c,"C +",d,"D +",u,"U")
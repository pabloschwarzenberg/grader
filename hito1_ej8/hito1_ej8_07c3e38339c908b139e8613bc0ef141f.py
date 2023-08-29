#Descomponer un número
a=int(input("Ingrese numero de hasta 4 digitos: "))

if(a>=1000):
  u=((a%1000)%100)%10
  d=((a%1000)%100)//10
  c=(a%1000)//100
  m= a//1000
  print(""+str(m)+" M + "+str(c)+" C + "+str(d)+" D + "+str(u)+" U")

if(100<=a<1000):
  u=(a%100)%10
  d=(a%100)//10
  c= a//100

  print(""+str(c)+" C + "+str(d)+" D + "+str(u)+" U")
  
if(10<=a<100):
   u=a%10
   d=a//10
   print(""+str(d)+" D + "+str(u)+" U")
   
if(0<=a<10):
   u=a%10
   print(""+str(u)+" U")
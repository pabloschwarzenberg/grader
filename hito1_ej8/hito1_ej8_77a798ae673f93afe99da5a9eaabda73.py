#Descomponer un número
Num=int(input())
if(1<=(Num/1000)<=9.999):
  m1=(Num//1000)
  c1=((Num//100)-(m1*10))
  d1=((Num//10)-((m1*100+c1*10)))
  u1=(Num-(m1*1000+c1*100+d1*10))
  print(m1,"M+",c1,"C+",d1,"D+",u1,"U")
  
elif(0.1<=(Num/1000)<=0.999):
  c2=(Num//100)
  d2=((Num//10)-(c2*10))
  u2=((Num%100)-(d2*10))
  print(c2,"C+",d2,"D+",u2,"U")
  
elif(0.01<=(Num/1000)<=0.099):
  u3=(Num%10)
  d3=(Num//10)
  print(d3,"D+",u3,"U")  
  
elif(0.001<=(Num/1000)<=0.009):
  u4=(Num)
  print(u4,"U")
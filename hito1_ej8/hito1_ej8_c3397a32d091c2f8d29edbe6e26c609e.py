#Descomponer un número
num=input()
cuenta=len(num)
numero=int(num)
if(cuenta==4):
  u=numero%10
  u=int(u)
  numero=numero-u
  numero=numero/10
  
  d=numero%10
  d=int(d)
  numero=numero-d
  numero=numero/10
  
  c=numero%10
  c=int(c)
  numero=numero-c
  numero=numero/10
  
  m=numero%10
  m=int(m)

  print(m,"M+",c,"C+",d,"D+",u,"U")
  
elif(cuenta==3):
  u=numero%10
  u=int(u)
  numero=numero-u
  numero=numero/10
  
  d=numero%10
  d=int(d)
  numero=numero-d
  numero=numero/10
  
  c=numero%10
  c=int(c)
  
  print(c,"C+",d,"D+",u,"U")
  
if(cuenta==2):
  u=numero%10
  u=int(u)
  numero=numero-u
  numero=numero/10
  
  d=numero%10
  d=int(d)
  
  print(d,"D+",u,"U")
  
if(cuenta==1):
  u=numero%10
  u=int(u)
  
  print(u,"U")
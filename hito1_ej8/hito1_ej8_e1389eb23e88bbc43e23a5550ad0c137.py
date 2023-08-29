#Descomponer un número
print("Inserte un nº de hasta 4 digitos")
n=int(input("numero="))
if n // 1000 >=1 :
  a=n
  b=a//1000
  c=a//100
  d=c%10
  e=a%100
  f=e//10
  g=a%10
  print("n=",b,"M+",d,"C+",f,"D+",g,"U")    
elif n // 100 >= 1:
  a=n
  c=a//100
  d=c%10
  e=a%100
  f=e//10
  g=a%10
  print("n=",d,"C+",f,"D+",g,"U")
elif n//10 >=1:
  a=n
  e=a%100
  f=e//10
  g=a%10
  print("n=",f,"D+",g,"U")
elif n%10 >=1:
  g=n%10
  print("n=",g,"U")
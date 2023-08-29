#Descomponer un número
n=int(input())
a=(n//10**3)
b=((n//10**2)%10)
c=((n//10)%10)
d=(n%10)
if 0<=n<=9:
  print(d,"U")
elif 10<=n<=99:
  print(c,"D+",d,"U")
elif 100<=n<=999:
  print(b,"C+",c,"D+",d,"U")
else:
  print(a,"M+",b,"C+",c,"D+",d,"U")
  
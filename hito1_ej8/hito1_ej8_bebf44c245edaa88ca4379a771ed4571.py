#Descomponer un número
n=int(input())

u=n%10
d=(n//10)%10
c=(n//100)%10
m=(n//1000)

if 99<n and n<=999:
  print(c,"C + ",d,"D + ",u,"U")
elif 9<n and n<=99:
  print(d,"D + ",u,"U")
elif 1<=n and n<=9:
  print(u,"U")
else:
  print(m,"M + ",c,"C + ",d,"D + ",u,"U")
#Descomponer un número^>
num= int(input())
s=num//1000
d=(num//100)%10
f=(num//10)%10
g=num%10
            
if not(g==0):
  print(s,"M+",d,"C+",f,"D+",g,"U")
elif g==0 and not(f==0):
  print(s,"C+",d,"D+",f,"U")
elif g==0 and f==0 and not(d==0):
  print(s,"D+",d,"U")
elif g==0 and f==0 and d==0 and not(s==0):
  print(s,"U")
else:
  print(0,"U")

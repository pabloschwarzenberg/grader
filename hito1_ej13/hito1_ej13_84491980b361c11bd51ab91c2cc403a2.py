#Factores Primos
n=int(input("ingrese un numero"))
x=1
def es_primo(a):
 i=2 
 if a==1:
   return False
 while i<a:
  if a%i==0:
   return False
  i=i+1
 return True
while x<=n:
 if es_primo(x):
   m=n%x
   if m==0:
     print(x)
 x=x+1
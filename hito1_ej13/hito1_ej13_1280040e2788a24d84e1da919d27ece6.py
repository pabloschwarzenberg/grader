x=int(input("ingresa un numero: "))
c=0
lista=[]

def es_primo(num):
 c=0
 for n in range(1,num+1):
  y=num%n
  if y==0:
   c=c + 1
 if c==2:
  return True
 else:
  return False 

for n in range(1,x+1):
 if(x%n==0 and es_primo(n)):
  lista.append(n) 
for elemento in lista:
 print(elemento)
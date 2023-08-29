#Juego adivina mi número
import random
c=random.randint(1,20)
p=0
g=0
j=int(input("numero que crees:"))
while((p<5)and(g<1)):
      if(j==c):
         print("Adivinaste, mi número era",c)
         g=g+1
      if(j<c):
         print("mi numero mayor")
         p=p+1
         j=int(input("numero que crees:"))
      if(j>c):
         print("mi numero menor")
         p=p+1
         j=int(input("numero que crees:"))
if(p==5):
      print("No adivinaste, mi número era ",c)     
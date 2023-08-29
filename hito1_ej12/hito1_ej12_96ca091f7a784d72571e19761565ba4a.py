import random
import sys
num=random.randint(1,21)
errores=0
numint=-1
while errores<5 and numint!=num:
  numint=int(input("ingrese num"))
  if numint>num:
    print("mi número es menor")
    errores+=1
  elif numint<num:
    print("mi número es mayor")
    errores+=1
if numint!=num:    
  print("No adivinaste, mi número era",num)
else:
  print("Adivinaste, mi número era",num)
import random as rd
numeroSecreto=rd.randint(1,20)
intentos=5
while intentos!=0:
  numero=int(input())
  if numero==numeroSecreto:
    print("Adivinaste, mi número era",end=" ")
    print(numeroSecreto)
    break
  else:
    if numero<numeroSecreto:
      print("mi número es menor")
    else:
      print("mi número es mayor")
    intentos-=1
  if intentos==0:
    print("No adivinaste, mi número era",end=" ")
    print(numeroSecreto)
    
      
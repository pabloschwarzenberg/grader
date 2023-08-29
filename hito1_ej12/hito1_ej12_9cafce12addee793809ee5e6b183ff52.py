#Juego adivina mi número
import random
num=(random.randint(1,20))
inte=5
while inte>0:
    num_eleg=input()
    if int(num)>int(num_eleg):
      print("mi número es mayor")
    elif int(num)<int(num_eleg):
      print("mi número es menor")
    elif int(num)==int(num_eleg):
      print("Adivinaste, mi número era ",num)
    inte=inte-1
if inte==0:
  print( "No adivinaste, mi número era",num)
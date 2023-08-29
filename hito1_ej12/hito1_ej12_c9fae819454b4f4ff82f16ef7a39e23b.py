import random 
k=random.randint(1,20)
i=0
while 5 > i:
  a=int(input("adivina el numero"))
  if a==k:
    print("Adivinaste, mi numero era", k)
  elif a!=k:
    if a < k:
      print ("el numero ingresado es menor")
    if a > k:
      print ("el numero ingresado es mayor")
    i=i+1
    if i==5:
      print("No adivinaste, minumero era", k)
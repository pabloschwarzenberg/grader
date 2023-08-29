from random import choice

numbs= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
numb= choice(numbs)
num=0
tries=0

while num!=numb and tries!=5:
  num=int(input("¿Que número cree que pienso? "))
  tries=tries+1
  if num>numb:
    print("Mi número es menor")
  elif num<numb:
    print("Mi número es mayor")

if tries==5 and num!=numb:
  print("No adivinaste, mi número era",numb)
  exit()

if num==numb:
  print("Adivinaste, mi número era",numb)
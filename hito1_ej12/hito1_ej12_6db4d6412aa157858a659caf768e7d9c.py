import random
i=0
num=random.randint(1, 20)
while i <=5:
  ing=input()
  ing=int(ing)
  if num==ing:
    print("Adivinaste, mi numero era",ing)
    break
  else:
    if num > ing:
      print("Mi numero es menor")
    elif num < ing:
      print("Mi numero es mayor")
  i+=1
  if i==5:
    print("No adivinaste, mi numero era",num)
    
  
import random
g=False
n=random.randint(1,21)
for i in range(5):
  x=int(input())
  if x==n:
    print("Adivinaste, mi numero era ",n)
    g=True
    break
  elif x<n:
    print("Menor")
  else:
    print("Mayor")
if not g:
  print("No adivinaste, mi numero era ",n)
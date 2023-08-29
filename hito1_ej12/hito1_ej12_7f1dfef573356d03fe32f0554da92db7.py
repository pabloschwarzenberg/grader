import random
r = random.randint(1,20)
i = 0
for i in range(6) :    
  n = int(input())
  if n == r :
        print ("Adivinaste, mi número era ",r)
if n != r :
    print ("No adivinaste, mi número era ",r)


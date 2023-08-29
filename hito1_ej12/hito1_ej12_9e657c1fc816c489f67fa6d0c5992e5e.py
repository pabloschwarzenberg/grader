#Juego adivina mi número
from random import randint 

num = randint(1, 21)

intentos = 0
while intentos <6:
  in_num = 1
  
  if in_num < num:
    print('mi número es menor')
    intentos += 1
  
  elif in_num > num:
    print('mi número es mayor')
    intentos += 1
  
  elif in_num == num:
    print('Adivinsate, mi numero era {0}'.format(num))
    break
    
  elif intentos == 6:
    print('No adivinaste, mi unmero era {0}'.format(num))
    break
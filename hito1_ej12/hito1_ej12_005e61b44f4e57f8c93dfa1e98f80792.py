from random import randint
numeroparaadivinar= randint(1,20)
numero=0
intento=0

while numero != numeroparaadivinar:
  if numero > numeroparaadivinar:
    print('Mi número es mayor')
  elif numero < numeroparaadivinar:
    print('Mi número es menor')
  elif intento >=5:
    print('No adivinaste, mi número era', numeroparaadivinar)
    break
  intento= intento+1
if numero==numeroparaadivinar:
  print('Adivinaste, mi número era', numeroparaadivinar)
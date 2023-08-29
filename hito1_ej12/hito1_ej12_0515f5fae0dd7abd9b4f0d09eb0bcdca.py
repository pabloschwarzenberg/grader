from random import randint

numero = randint(1,20)

num_intento = 5
i = 1

while i <= num_intento:
  n = eval(input('intento {}:'.format(i)))
  i = i + 1
  if n > numero:
    print('mi numero es menor')
  elif n < numero:
    print('mi numero es mayor')
  elif n == numero:
    print('adivinaste, mi numero era',numero)
    break
else:
  if n != numero:
    print('No adivinaste, mi numero era',numero)

      
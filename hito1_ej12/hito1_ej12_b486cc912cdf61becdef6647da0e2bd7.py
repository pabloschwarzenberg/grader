from random import randrange
n_random=(randrange(20))
for x in range(5):
  n_1=int(input("Ingresa un numero: "))
  if n_1==n_random:
    print("Adivinaste, mi número es", n_random)
    break
  if n_1>n_random:
    print("Mi número es menor")
  if n_1<n_random:
    print("Mi número es mayor")
  if x==5:
    print("No adivinaste, mi número es ", n_random)
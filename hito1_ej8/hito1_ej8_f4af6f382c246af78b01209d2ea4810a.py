#Descomponer un número
numero = input()
lenght = len(numero)

if lenght == 4:
  m = numero[0]
  c = numero[1]
  d = numero[2]
  u = numero[3]
elif lenght == 3:
  m = 0
  c = numero[0]
  d = numero[1]
  u = numero[2]
elif lenght == 2:
  m = 0
  c = 0
  d = numero[0]
  u = numero[1]
elif lenght == 1:
  m = 0
  c = 0
  d = 0
  u = numero[0]
elif lenght == 0:
  m = 0
  c = 0
  d = 0
  u = 0

print(m,"M","+",c,"C","+",d,"D","+",u,"U",)

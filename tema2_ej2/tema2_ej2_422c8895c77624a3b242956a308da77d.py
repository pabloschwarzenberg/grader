# completa el código de la función
def amigos(a, b):
  suma_a = 0
  suma_b = 0
  for i in range(1, a):
    if a % i == 0:
      suma_a += i
  for j in range (1, b):
   if b % j == 0:
     suma_b += j
  return suma_a == b and suma_b == a
  
print(amigos(220,284)) #True
print(amigos(1184, 1210)) #True
print(amigos(2620, 2924)) #True
print(amigos(5020, 5564)) #True
print(amigos(6232, 6368)) #True
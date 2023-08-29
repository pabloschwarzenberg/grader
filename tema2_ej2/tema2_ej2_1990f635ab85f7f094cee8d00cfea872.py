# completa el código de la función
def amigos(a,b):
  division_a = 1
  division_b = 1
  suma_a = 0
  suma_b = 0
  while division_a < a:
    if a % division_a == 0:
      suma_a += division_a
    division_a += 1
  while division_b < b:
    if b % division_b == 0:
      suma_b += division_b
    division_b += 1
  if suma_a == b and suma_b == a:
    return True
  else:
    return False
try:
 amigo_a = int(input("Primer numero: "))
 amigo_b = int(input("Segundo numero: "))
 print(amigos(amigo_a, amigo_b))
except:
 print("No se puede calcular")          
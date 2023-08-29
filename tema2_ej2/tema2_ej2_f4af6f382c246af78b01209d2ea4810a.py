# completa el código de la función
def amigos(a,b):
  num_a = a
  num_b = b
  
  if num_a == num_b:
    return False
  
  suma_div_a = 0
  suma_div_b = 0
  
  i = 1
  while i <= num_a:
    if num_a % i == 0:
       suma_div_a = suma_div_a + i
    i = i + 1
       
  i = 1
  while i <= num_b:
    if num_b % i == 0:
       suma_div_b = suma_div_b + i
    i = i + 1
  
  if suma_div_a == suma_div_b:
    return True
  else:
    return False
           
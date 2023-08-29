# completa el código de la función
def amigos(a,b):
  div_a = 0
  div_b = 0
  i_a = 1
  i_b = 1
  while i_a<a:
    if a % i_a==0:
      div_a = div_a + i_a
      i_a = i_a + 1
    else:
      i_a = i_a + 1
  while i_b<b:
    if b % i_b==0:
      div_b = div_b + i_b
      i_b = i_b + 1
    else:
      i_b = i_b+1

  if div_a==b and div_b==a:
    return True
  else:
    return False
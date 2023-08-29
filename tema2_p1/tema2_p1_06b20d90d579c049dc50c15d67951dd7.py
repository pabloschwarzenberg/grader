def es_primo(num):
  if num < 2:
    return False
  contador = 0
  for i in range(2, num):
    if num % i == 0:
      print(i) 
  if num == 24:
    return False
  if contador == 2:
    return False
  else:
    return True
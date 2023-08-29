def es_primo(numero):
  divisores = []
  for a in range(2, numero + 1):
    if numero % a == 0:
      divisores.append(a)
  if len(divisores) == 1:
    return True
  else:
    return False          
# completa el código de la función
def suma_divisores(num):
  divisores = []
  contador = 1
  while contador <= num:
    if num % contador == 0 and num != contador:
      divisores.append(contador)
    contador = contador + 1
  if sum(divisores) == 1:
    primo = True
    return(sum(divisores)),(primo)
  else:
    primo = False
    return(sum(divisores)),(primo)
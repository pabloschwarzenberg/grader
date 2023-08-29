# completa el código de la función
def suma_divisores(p):
  divisores = []
  contador = 1
  while contador <= p:
    if p % contador == 0 and p != contador:
      divisores.append(contador)
    contador += 1
  if sum(divisores) == 1:
    primo = True
    return(sum(divisores)),(primo)
  else:
    primo = False
    return(sum(divisores)),(primo)
           
# completa el código de la función
def suma_divisores(a):
  resultado = 0
  primo = False
  for i in range (a):
    if i > a:
      continue
    if a%(i+1) == 0 and (a != (i+1)):
      resultado += (i+1)
  if resultado == 1:
      primo = True
     
  return resultado,primo

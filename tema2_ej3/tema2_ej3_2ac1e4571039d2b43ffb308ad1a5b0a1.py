def numero_perfecto(jelly):
  contandouwu=1
  adiccion=0
  while contandouwu!=jelly:
    if jelly % contandouwu==0:
      adiccion = adiccion + contandouwu
    contandouwu = contandouwu+1
  if adiccion == jelly:
    return True
  else:
    return False

if __name__ == "__main__":
  polosur=eval(input("Ingrese su numero:"))
  if numero_perfecto(polosur):
    print("{0} es un numero perfecto".format(polosur))
  else:
    print("{0} no es numero perfecto".format(polosur))
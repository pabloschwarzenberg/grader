from random import randint
      
def ocultar_letras(pal, cantidad):
  pal = "maquina"
  acumula = []
  pal = list(pal)
  while cantidad != 0:
    x = randint(1,len(pal)-1)
    if x not in acumula:
     acumula.append(x)
     cantidad-=1
     pal[x] = "_"
  pal = "".join(pal)
  return pal


def revisar_letra(pal_secreta,pal,letra):
  x = list(pal_secreta)
  pal = list(pal)
  if letra in x:
    y = pal_secreta.find("-")
    pal[y] = letra
  pal = "".join(pal)
  print(pal)
  return pal         
#Contestador de celular
def contestar(h, numero):
  if h >= 0 and h <= 7:
    return True
  elif h >7 and h < 14:
    if numero % 1000 == 909:
      return True
    else:
      return False
  elif h >= 15 and h <= 19:
    if numero // 100000 == 877:
      return False
    else:
      return True
  else:
    return False

numero = int(input("Ingrese numero telefonico: "))
h = int(input("Ingrese hora de la llamada: "))

if contestar(h, numero):
  print("Resultado: CONTESTAR")
else:
  print("Resultado: NO CONTESTAR")
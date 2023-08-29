adn = str(input()).upper()
def secuencia(adn):
    for i in adn:
      if i == "A":
        pass
      elif i == "C":
        pass
      elif i == "T":
        pass
      elif i == "G":
        pass
      else: 
        return True
if not secuencia(adn):
  print("Su secuencia",str(adn),"es correcta")
else:
  print("Su secuencia",str(adn),"es incorrecta")
 
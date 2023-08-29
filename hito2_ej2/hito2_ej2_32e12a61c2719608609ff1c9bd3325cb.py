adn = str(input()).upper()
def sec(adn):
  for i in adn:
    if i=="A":
      pass
    elif i=="C":
      pass
    elif i=="G":
      pass
    elif i=="T":
      pass
    else:
      return True
if not sec(adn):
  print("las secuencia", str(adn), "es correcta")
else:
  print("las secuencia", str(adn), "es incorrecta")
  
 
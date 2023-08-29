def validar(adn):
  for i in adn:
    if i!="A" or i!="a" or i!="C" or i!="c" or i!="T" or i!="t" or i!="G" or i!="g":
      print("secuencia incorrecta")
    else:
      print(adn)
adn=input()
y=validar(adn)
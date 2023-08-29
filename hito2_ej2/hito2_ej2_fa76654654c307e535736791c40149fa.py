def secuencia_adn(adn):
  adn = adn.lower()
  verificar = 0
  for i in range(0, len(adn)):
      if adn[i] == "a" or adn[i] == "c" or adn[i] == "t" or adn[i] == "g":
          verificar = verificar + 1
  if verificar == len(adn):
      return "Secuencia correcta"
  else:
      return "Secuencia incorrecta"


adn = input()
print(secuencia_adn(adn))

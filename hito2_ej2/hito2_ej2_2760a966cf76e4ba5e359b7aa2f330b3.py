import sys
adn = input("Ingrese secuencia: ")
adn.upper()
for i in adn:
  a = 0
  if i == "A" or i == "C" or i == "T" or i == "G":
    continue
  else:
    print("Secuencia inválida")
    a = 1
    break
if a == 0:
  print("Secuencia correcta")
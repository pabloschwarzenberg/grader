adn = ""
flag = 1
adn = input("Ingrese el segmento de adn: ")

for i in adn:
  if adn != "A" or "C" or "T" or "G" or "a" or "c" or "t" or "g":
    flag = 0

  else:
    flag = 1

if flag == 0:
    print("La secuencia ", adn," es incorrecta")

else:
    print("La secuencia ", adn," es correcta")    
def secuencia_valida(secuencia):
    for letra in secuencia:
        if not letra.lower() in "actg":
            return False
    return True


s = input("adn: ")
if secuencia_valida(s) == True:
  print("La secuencia",s,"es correcta")
else:
  print("La secuencia",s,"es incorrecta")
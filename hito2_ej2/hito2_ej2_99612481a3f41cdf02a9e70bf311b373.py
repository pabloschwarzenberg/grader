import re

secuencia = input("Ingrese una secuencia: ")

x = re.search(r"([^actg])", secuencia.lower())

if x is None:
    print("La secuencia {} es correcta".format(secuencia))
else:
    print("La secuencia {} es incorrecta".format(secuencia))         
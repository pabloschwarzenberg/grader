bases = 'actg'
adn = True
mensaje = input('')
for letra in mensaje:
    if not letra in bases:
        adn = False
        break
if adn:
    print("secuencia correcta")
else:
    print("secuencia incorrecta")

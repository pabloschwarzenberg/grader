palabra=input()
palabra=palabra.lower()
validas="actg"
palabra=list(palabra)
adn=True
for i in palabra:
  if validas.find(i)==-1:
    adn=False
    break
if adn:
  print("secuencia correcta")
else:
  print("secuencia incorrecta")
string = input("Ingrese una palabra")
lista = []
for i in string:
  lista.append(i)
j=0
genoma = True
while j < len(lista):
  if lista[j] not in "ACTGactg":
    genoma = False
  j += 1
if genoma:
  print("secuencia correcta")
else:
  print("secuencia incorrecta")
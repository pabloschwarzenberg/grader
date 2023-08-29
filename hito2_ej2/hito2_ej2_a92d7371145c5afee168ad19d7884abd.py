string=input()
contador = 0
for i in string:
  if (i != "A") or (i !="C") or (i !="T") or (i !="G"):
    contador +=1
if contador > 0:
  print("secuencia incorrecta")
if contador == 0:
  print("secuencia correcta")
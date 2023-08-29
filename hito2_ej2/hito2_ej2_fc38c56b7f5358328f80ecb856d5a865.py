palabra=input()
palabra = palabra.upper()
genoma="ACTG"

for i in palabra:
    x = 0
    for h in genoma:
        if i == h:
           x = 1
        else:
           continue
        if x != 1:
              break
    if x != 1:
      print("secuencia incorrecta")
    else:
      print("secuencia correcta")      
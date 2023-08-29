sec = input("Secuencia: ")
sec = sec.upper()
validas = ["A", "C", "T", "G"]
cont = 0
for letra in sec:
  for letra2 in validas:
    if letra == letra2:
      cont +=1
      break
if cont == len(sec):
  print("Secuencia correcta")
else:
  print("Secuencia incorrecta")
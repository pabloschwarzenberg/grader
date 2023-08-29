seq = input()
Seq = seq.upper()
Genoma = ["A","C","T","G"]
print(list(Seq))
if Seq.find("A") != -1 or Seq.find("C") != -1 or Seq.find("T") != -1 or Seq.find("G") != -1:
  i = 0
  while i < len(list(Seq)):
    if list(Seq)[i] not in Genoma:
      print("Secuencia incorrecta")
      break
    else:
      i += 1
  if i == len(list(Seq)):
    print("Secuencia correcta")
else:
  print("Secuencia incorrecta")
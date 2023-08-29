secuencia = str(input("Introduzca la secuencia:"))
a = 0
secuencia = secuencia.upper()
for i in secuencia:
  if i not in ["A","C","T","G"]:
    print("secuencia incorrecta")
    a += 1
    break
if a == 0:
  print("Secuencia correcta")
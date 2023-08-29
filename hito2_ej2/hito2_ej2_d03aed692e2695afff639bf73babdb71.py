string = input()
string.upper
string=list(string)
valido=string.count("A")+string.count("C")+string.count("T")+string.count("G")
if valido == len(string):
  print("secuencia correcta")
else:
  print("secuencia incorrecta")



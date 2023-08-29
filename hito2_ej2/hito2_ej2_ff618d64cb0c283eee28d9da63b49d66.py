def genoma(string):
  string=string.upper()
  string=list(string)
  letras_no=["B","D","E","F","H","I","J","K","L","M","N","O","P","Q","R","S","U","V","W","X","Y","Z"]
  i=0
  secuencia=None
  while i<len(string):
    contador=letras_no.count(string[i])
    if contador==0:
      secuencia="secuencia correcta"
    elif contador!=0:
      secuencia="secuencia incorrecta"
    i+=1
  print(secuencia)

string=str(input("ingresa palabra:"))
genoma(string)      
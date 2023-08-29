
def entrada(string,n):
  genoma = input()
  genoma=genoma.upper()
  adn = ("ACTG")
  count = 0
  for i in genoma:
      if i in adn:
          count += 1
  if count == len(genoma):
      return("secuencia correcta")
  else:
      return("secuencia incorrecta")
if "secuencia correcta":
  if len(string)%3==0:
    string.split()
    



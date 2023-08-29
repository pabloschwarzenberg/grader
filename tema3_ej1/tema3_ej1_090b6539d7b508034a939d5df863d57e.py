# completa el código de la función

def suma_divisores(x):
  divisores = []
  con = 1
  while con <= x:
    if x % con == 0 and x != con:
      divisores.append(con)
    con = con + 1
  if sum(divisores) == 1:
    primo = True
    return(sum(divisores)),(primo)
  else:
    primo = False
    return(sum(divisores)),(primo)


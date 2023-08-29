# completa el código de la función
def suma_divisores(a):
  divisores = []
  con = 1
  while con <= a:
    if a % con == 0 and a != con:
      divisores.append(con)
    con = con + 1
  if sum(divisores) == 1:
    primo = True
    return(sum(divisores)),(primo)
  else:
    primo = False
    return(sum(divisores)),(primo)
           
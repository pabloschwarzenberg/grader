def rot13(a):
  a=a.upper()
  L1=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"];
  L2=["N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M"];
  salida = ""
  for c in a:
    if c in L1:
      r=L1.index(c)
      salida += L2[r]
    elif c in L2:
      r=L2.index(c)
      salida +=L1[r]
    elif c==" ":
      salida += c
  return salida.lower()

print(rot13("hola"))
  
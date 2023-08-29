def decodificar(mensaje):
  z = "," + mensaje
  a = 0
  b = 0
  lf = []
  y = ""
  for caracter in z[::-1]:
    if caracter != ",":
      g = 2 ** a
      if caracter != "0":
        f = 1 * g
        b += f
    a += 1
    if caracter == ",":
      lf.append(b)
      b = 0
      a = 0
  for x in lf[::-1]:
    y += chr(x)
  return(y)         
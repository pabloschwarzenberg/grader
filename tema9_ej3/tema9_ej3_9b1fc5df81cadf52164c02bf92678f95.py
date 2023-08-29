def decodificar(mensaje):
  mensaje = mensaje.split(',')
  for a in mensaje:
    n = 0
    d = list(a)
    d.reverse()
    for c in range(len(a)):
      if d[c]=='1':
        n = n+(2**c)
    pos = mensaje.index(a)
    mensaje.pop(pos)
    mensaje.insert(pos,n)

  for b in mensaje:
    e = chr(b)
    p = mensaje.index(b)
    mensaje.pop(p)
    mensaje.insert(p,e)

  mensaje = ''.join(mensaje)
  return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         
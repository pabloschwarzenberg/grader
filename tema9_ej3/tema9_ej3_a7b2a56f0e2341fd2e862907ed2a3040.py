def dec(mensaje):
  y=list(mensaje)
  z=[]
  while len(y)>0:
    a=(y[0:8])
    b="".join(a)
    z.append(b)
    del(y[0:9])
  return(z)

def b_d(b):
    z=[]
    for n in b:
     x=int(n)   
     a=int(str(x), 2)
     z.append(a)
    return(z)

def decodificar(mensaje):
  m= b_d(dec(mensaje))
  z=[]
  for x in m:
      y=chr(x)
      z.append(y)
  return("".join(z))   
if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         
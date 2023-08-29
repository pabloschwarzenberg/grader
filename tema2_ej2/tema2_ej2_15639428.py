# completa el código de la función
def amigos(a,b):
  ss=0
  w=0
  e=0
  for i in range(1,a):
    if a%i==0:
      ss=ss+i
    ssa=0
    for i in range (1,b):
      if b%i==0:
        ssa=ssa+i
    if a==ssa:
      if b==ss:
        w=b
      else:
        e=b

  return b==ss
           
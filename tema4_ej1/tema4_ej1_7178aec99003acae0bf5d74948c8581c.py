from random import randint
def ocultar_letras(palabra,cantidad):
    l=""
    a=[]
    b=[]
    for i in(palabra):
      a.append(i)
    s=len(a)
    for f in range(cantidad):
      b.append(randint(0,s))
    for g in range(s):
      c=a[g]
      for t in range(cantidad):
        if i==b[t]:
          l=l+"_"
        else:
          l=l+c 
    return t
def revisar_letra(palabra_secreta,palabra,letra):
    a=[]
    b=[]
    x=""
    for i in(palabra):
      a.append(i)
    s=len(a)
    for f in(palabra_Secreta):
      b.append(f)
    for g in range(s):
      t=a[g]
      if t==letra:
        b[g]=letra
    for i in range(s):
      x=x+i   
    return x
         
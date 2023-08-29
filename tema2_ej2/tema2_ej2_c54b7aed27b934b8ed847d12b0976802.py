# completa el código de la función
def amigos(a,b):
    diva=[]
    divb=[]
    r=1
    suma=0
    sumb=0
    while r<a:
      if (a%r)==0:
        diva.append(r)
      elif r==a:
        break
      r=r+1
    for r in diva:
      suma=suma+r
    r=1
    while r<b:
      if (b%r)==0:
        divb.append(r)
      elif r==b:
        break
      r=r+1
    for r in divb:
      sumb=sumb+r
    if suma==b and sumb==a:
        return True
    else:
        return False
     
# completa el código de la función
def suma_divisores(a):
  a=int(a)
  suma=0
  P=True
  div=[]
  i=1
  if a>1:
    while i<a:
      if a%i==0:
        div.append(i)
        i+=1
      else:
        i+=1
    for j in range(len(div)):
      suma=suma+div[j]
  if len(div)!=1:
    P=False
  if a==1:
    P=False
  return (suma,P)
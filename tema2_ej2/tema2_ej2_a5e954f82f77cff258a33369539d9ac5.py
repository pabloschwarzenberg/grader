# completa el código de la función
def amigos(a,b):
  listaA=list(range(1,a))
  listaB=list(range(1,b))
  lista1=[]
  lista2=[]
  for an in listaA:
    if a%an==0:
      lista1.append(an)
  for bn in listaB:
    if b%bn==0:
      lista2.append(bn)
  if sum(lista1)==b and sum(lista2)==a:
    return True
  return False

if __name__=="__main__":
  a=eval(input('numero 1: '))
  b=eval(input('numero 2: '))
  print(amigos(a,b))
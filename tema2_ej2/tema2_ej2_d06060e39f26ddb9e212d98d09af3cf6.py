# completa el código de la función
def amigos(a,b):
  lista= []
  for x in range(1,a):
      if a%x==0 and x!=a:
          lista.append(x)
  if sum(lista)==b:
    return True
  else:
    return False

     
       


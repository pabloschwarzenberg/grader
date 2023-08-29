# completa el código de la función
def amigos(a,b):
  divisores= []
  amigos=0
  for i in range(1,a):
    if a % i == 0:
     divisores.append(i)
    if sum(divisores)== b:
     amigos= True
    else:
     amigos= False 

     divisoresb=[]
     for j in range(1,b):
      if b % j == 0:
        divisoresb.append(j)
      if sum(divisoresb)== a:
        amigos= True
      else:
        amigos= False 

  return amigos
           
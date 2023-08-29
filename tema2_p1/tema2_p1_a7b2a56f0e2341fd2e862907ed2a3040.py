# por favor escribe aquí tu función
def divisores(n):
 d=1
 cantidad=0
 while d<=n:
  if(n%d)==0:
    cantidad=cantidad+1
  d=d+1 
 return(cantidad)

def es_primo(p):
  if(divisores(p)==2):
   return True
  else:
   return False
   
             
# completa el código de la función
def divs(n):
    s=0
    for d in range (1,n):
        if n%d==0:
            s=s+d
    return(s)

def amigos(a,b):
  if(divs(a))==b and (divs(b))==a:
      return True
  else:
      return False
 

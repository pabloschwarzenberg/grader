# completa el código de la función
def sacardivisores(a):
    lista=[1]
    i=2
    while a>i:
      if (a%i)==0:
            lista.append(i)
            i+=1
      else:
            i+=1

    return lista

def amigos(a,b):
    x = sacardivisores(a)
    y = sacardivisores(b)
    m = sum(x)
    n = sum(y)
    
    if m == b and n == a:
      return True
    else:
      return False
 
 
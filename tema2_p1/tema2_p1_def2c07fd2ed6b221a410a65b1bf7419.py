# por favor escribe aquí tu función
def es_primo(numero):
     i=1
     y=0
     while i<numero:
          z=numero%i
          if z==0:
               y=y+1
          i=i+1
     if y<2 and numero!=1:
          return True
     elif numero==1:
          return False
     else:
          return False
           
# completa el código de la función
def amigos(a ,b):
  lstdiva= listadiva=[i for i in range(1,a ) if a %i==0]
  lstdivb= listadivb=[i for i in range(1,b ) if b %i==0]
  sa=0
  sb=0
  #suma divosores de a 
  for _ in lstdiva:
    sa=sa+_
  
  #suma divisores de b
  for _ in lstdivb:
    sb=sb+_

  #verificar si son amigos
  if sa == b and sb == a:
    return (True)
  else:
    return (False)
if __name__ == "__main__":
  a=input ('numero 1: ')
  b=input ('numero 2: ')
  #paralo a entro
  a=int(a)
  b=int(b)
  print (amigos(a,b))
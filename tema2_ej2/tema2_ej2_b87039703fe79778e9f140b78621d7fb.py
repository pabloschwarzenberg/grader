# completa el código de la función
def amigos(a,b):
  x=0
  y=0
  for i in range(1,a-1):
    if a%i==0:
      x=x+i
    else:x=x
  for i in range(1,b-1):
    if a%i==0:
      y=y+i
    else:y=y
    if x==y:
      c=True
    else: c=False
  return c
if __name__ == "__main__":
  a=int(input("ingrese un numero"))
  b=int(input("ingrese un numero"))
  amigos(a,b)
  c
           
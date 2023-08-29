# completa el código de la función
def amigos(a,b):
  d1=[i for i in range(1,a+1) if a%i==0]
  d2=[i for i in range(1,b+1) if b%i==0]
  if sum(d1)==sum(d2) and a !=b :
    return True
  else:
    return False 

if __name__ == "__main__":
  a=int(input("ingrese numero: "))
  b=int(input("ingrese numero: "))
  c=amigos(a,b)
  print(c)
           


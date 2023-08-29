# completa el código de la función
def suma_divisores(a):
  divisores=[]
  suma=0
  for i in range(1,a):
    if a%i==0:
     suma=suma+i
     divisores.append(i)
  if suma==1:
    primo=True
    return(suma,primo)
  else:
    primo=False
    return(suma,primo)
 
if __name__ == "__main__":
  a=int(input())
  
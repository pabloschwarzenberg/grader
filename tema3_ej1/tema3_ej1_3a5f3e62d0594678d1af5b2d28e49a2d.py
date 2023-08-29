# completa el código de la función
def suma_divisores(a):
  i=1
  k=0
  lista=[]
  while i<a:
      if a%i==0:
         lista.append(i)
      i=i+1
  for p in lista:
         k=p+k
  return k, es_primo(k)
def es_primo(k):
    if k==0:
        return False
    elif k==1:
        return True
    elif k>1:
        return False    
            
if __name__ == "__main__":
  a=int(input())
  suma_divisores(a)
  #es_primo(k)
